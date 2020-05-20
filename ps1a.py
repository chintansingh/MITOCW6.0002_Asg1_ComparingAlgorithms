###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Chintan Singh
# Collaborators: None
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    
    
    infile = open(filename, 'r') 
    
        
    dict = {}
    
    for line in infile:
        name,wt = line.split(",") #take each line in two variables
        
        dict[name] = int(wt) # create dictionary, convert wt from str to int
        
    return dict
        

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    
    dict = cows.copy() #shallow copy
    
    #sort to list using lambda in O(n*log n) time
    sorted_cows = sorted(dict.items(),key = lambda x:(x[1],x[0]), reverse = True)
    
    # Loop variables
    
    output = []                #tranches are appended to this final output
    

    while len(sorted_cows) > 0:
        tranche = []           #set of cows in each trip
        idx_to_delete = []     #to delete cows in tranche from dictionary
        payload = 0            #to check each tranche's weight
        
        for i in range(len(sorted_cows)):
            
            if (payload + sorted_cows[i][1] <= limit):
                tranche.append(sorted_cows[i][0])
                idx_to_delete.append(i)
                payload += sorted_cows[i][1]
                
            
        output.append(tranche)
        
        for j in idx_to_delete[::-1]:
            del(sorted_cows[j])
        
    return output
        
# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    
    partitions = []
    
    #Creating a list of possible partitions
    for partition in get_partitions(cows):
        partitions.append(partition)
        
    
    partitions = sorted(partitions,key=lambda x:len(x))
        
    
    combo = 0
    ''' partitions is the set of all possible combinations.
    Each combination has one or many tranches of cows that travel together
    Each tranche has individual cows'''
    for combination in partitions:
        combination_failed = False
        combo += 1
        for tranche in combination:
            
            payload = 0
            
            for i in tranche:
                payload += cows[i]
                
            if payload > limit:
                combination_failed = True
                continue
        if combination_failed:
            continue
        else:
            
            return combination
        
                
    
            
            
                
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass

cows = load_cows("ps1_cow_data.txt")
print(cows)

start = time.time()

for i in range(10,20):
    
    g = greedy_cow_transport(cows,i)
    print("Greedy: Max Load: ",i, "length: ", len(g))

end = time.time()    

print("Time for Greedy: ", end-start)
print()


start = time.time()

for i in range(10,20):
    
    b = brute_force_cow_transport(cows,i)
    print("Brute Force: Max Load: ",i, "length: ", len(b))

end = time.time()    
print("Time for Brute Force: ", end-start)

