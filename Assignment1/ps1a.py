###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Greedies
# Collaborators: Ali Çolak, İsmail Şengül, Abdeljalil Azganin, Yaşar Burcu Açan
# Time: 18/03/2024 Spring 2024 

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
            if current_limit == 0 : 
                break
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

    set_of_partitions = get_partitions(cows)
    possible_trips = []

    for partition in set_of_partitions:
        flag = True
        for set in partition:
            counter = 0
            for cow in set : 
                counter += cows[cow]
                if counter > 10:
                    flag = False
                    break          
        if flag : 
            possible_trips.append(partition)
    
    minTripsCount = len(possible_trips[0])
    minTrip = possible_trips[0]
    
    for trip in possible_trips : 
        if len(trip) < minTripsCount : 
            minTripsCount = len(trip)
            minTrip = trip

    return minTrip    

        
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

    filename = 'ps1_cow_data.txt'
    cows = load_cows(filename)

    # Greedy Cow Transport
    start_time = time.time()
    greedy_result = greedy_cow_transport(cows)
    end_time = time.time()
    greedy_time = end_time - start_time
    print("Greedy Cow Transport:")
    print(f"Number of trips: {len(greedy_result)}")
    print(f"Time taken: {greedy_time} seconds\n")
    # print(f"Greedy Result: {greedy_result} \n")


    # Brute Force Cow Transport
    start_time = time.time()
    brute_force_result = brute_force_cow_transport(cows)
    end_time = time.time()
    brute_force_time = end_time - start_time
    print("Brute Force Cow Transport:")
    print(f"Number of trips: {len(brute_force_result)}")
    print(f"Time taken: {brute_force_time} seconds")
    # print(f"Brute Force Result: {greedy_result} \n")


# Improved Problem Enemy Cow
 
def load_enemy_cows(filename):
    enemy_cow_data = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('=')
            cow_name = parts[0].strip()
            if len(parts) > 1 and parts[1].strip() != '':
                enemies = [enemy.strip() for enemy in parts[1].split(',')]
            else:
                enemies = []
            enemy_cow_data[cow_name] = enemies
    return enemy_cow_data   

def greedy_enemy_cow_transport(cows,enemy_cows,limit=10):

    sorted_cows = OrderedDict(sorted(cows.items(),key=lambda x:x[1],reverse=True))
    trips = []

    while sorted_cows:
        current_limit = limit
        current_trip = []
        current_cows = []
      
        for cow, weight in sorted_cows.items():
            if current_limit == 0 : 
                break
            if(weight <= current_limit):
                flag = True

                for enemy in enemy_cows[cow] :
                    if enemy in current_cows:
                        flag = False
                        print("Enemy found",cow,enemy)
                        break
                if flag : 
                    current_limit = current_limit - weight
                    current_trip.append({cow:weight})
                    current_cows.append(cow)
                    sorted_cows = removekey(sorted_cows,cow)    

        trips.append(current_trip)   

    return trips

def brute_force_enemy_cow_transport(cows,enemy_cows,limit=10):

    set_of_partitions = get_partitions(cows)
    possible_trips = []

    for partition in set_of_partitions:
        flag = True
        for set in partition:
            counter = 0
            for cow in set : 
                counter += cows[cow]
                if counter > 10:
                    flag = False
                    break
                for enemy in enemy_cows[cow] :
                    if enemy in set: 
                        flag = False 
                        break        
        if flag : 
            possible_trips.append(partition)
    
    minTripsCount = len(possible_trips[0])
    minTrip = possible_trips[0]
    
    for trip in possible_trips : 
        if len(trip) < minTripsCount : 
            minTripsCount = len(trip)
            minTrip = trip

    return minTrip 

def compare_enemy_cow_transport_algorithms():
   
    filename = 'ps1_cow_data.txt'
    cows = load_cows(filename)

    filename_enemy = 'ps1_enemy_cow_data.txt'
    enemy_cows = load_enemy_cows(filename_enemy)

    # Greedy Enemy Cow Transport
    start_time = time.time()
    greedy_result = greedy_enemy_cow_transport(cows,enemy_cows)
    end_time = time.time()
    greedy_time = end_time - start_time
    print("Greedy Enemy Cow Transport:")
    print(f"Number of trips: {len(greedy_result)}")
    print(f"Time taken: {greedy_time} seconds\n")
    # print(f"Greedy Result: {greedy_result} \n")

    # Brute Enemy Force Cow Transport
    start_time = time.time()
    brute_force_result = brute_force_enemy_cow_transport(cows,enemy_cows)
    end_time = time.time()
    brute_force_time = end_time - start_time
    print("Brute Force Enemy Cow Transport:")
    print(f"Number of trips: {len(brute_force_result)}")
    print(f"Time taken: {brute_force_time} seconds")    
    # print(f"Brute Force Result: {greedy_result} \n")


def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def main():

    """

    ########### Problem 1 ############
    
    filename = 'ps1_cow_data.txt'
    cow_dict = load_cows(filename)
    # print(cow_dict)
    
    ########### Problem 2 ############
    
    greedy_choosen = greedy_cow_transport(cow_dict)
    print("Minimum Transport Count with Greedy : " , len(greedy_choosen))
    # print("Minimum Transport with Greedy : " , greedy_choosen)


    ########### Problem 3 ############
    
    brute_fort_choosen = brute_force_cow_transport(cow_dict)
    print("Minimum Transport Count with Brute Force : " , len(brute_fort_choosen))
    # print("Minimum Transport with Brute Force : " , brute_fort_choosen)

    """

    ########### Problem 4 ############

    compare_cow_transport_algorithms()

    ########### Improved Problem Enemy Cow ############
    
    compare_enemy_cow_transport_algorithms()

    
if __name__ == "__main__":
    main()    