###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
from collections import OrderedDict

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
    cow_data = {}
    with open(filename, 'r') as file:
        for line in file:
            name, weight = line.strip().split(',')
            cow_data[name] = int(weight)
    return cow_data

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


    sorted_cows = OrderedDict(sorted(cows.items(),key=lambda x:x[1],reverse=True))
    trips = []

    while sorted_cows:
        current_limit = limit
        current_trip = []
      
        for cow, weight in sorted_cows.items():
            if(weight <= current_limit):
                current_limit = current_limit - weight
                current_trip.append({cow:weight})
                sorted_cows = removekey(sorted_cows,cow)

        trips.append(current_trip)   

    return trips

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

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def main():
    ########### Problem 1 ############
    
    filename = 'ps1_cow_data.txt'
    cow_dict = load_cows(filename)
    # print(cow_dict)
    
    ########### Problem 2 ############
    
    greedy_choosen = greedy_cow_transport(cow_dict)
    print("Minimum Transport with Greedy : " , len(greedy_choosen))
    # print(greedy_choosen)

    
    
    greedy_cow_transport(cow_dict)
if __name__ == "__main__":
    main()