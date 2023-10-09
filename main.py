
from fileLoader import *
from truck import *
from datetime import *
from hashTable import *
from package import *


# Nearest neighbor function
def find_nearest(distances: [[]], addresses, truck):
    # Creating the list of truck specific package ids and initializing a list of truck specific address indexes
    packages = truck.get_package_list()
    truck_addresses = []

    # Creating list of truck specific address indexes
    for address in addresses:
        for this_package_id in packages:
            if address == my_hash_table.search_hash_table(this_package_id).address:
                truck_addresses.append(address_lookup(address))
    truck_addresses = set(truck_addresses)

    # Initialization values for looping
    addresses_visited = [0]
    final_addresses = [0]
    index = 0
    new_index = 0

    # Finding the minimum distance from each location, starting from the hub, and keeping track of each location and
    # distance within the final_addresses list
    for i in range(len(distances)):
        this_min_distance = 50
        for j in range(len(distances)):
            if distances[index][j] < this_min_distance and j not in addresses_visited and j in truck_addresses:
                this_min_distance = distances[index][j]
                new_index = j
        if new_index != index:
            index = new_index
            addresses_visited.append(index)
            final_addresses.append([index, this_min_distance])
            distances[i][index] = 50
            distances[index][i] = 50

    final_addresses.append([0, distances[0][index]])

    # Removing the initial hub index and returning the list of ordered address indexes
    final_addresses.pop(0)
    return final_addresses


# Address lookup function to return index in address list of specified address
def address_lookup(address):
    for i in range(len(address_list)):
        if address_list[i] == address:
            return i


# Translation of time in decimal form to datetime time class form
def decimal_time_translation(decimal_time):
    this_hour = int(decimal_time)
    this_minute = int((decimal_time - this_hour) * 60)
    this_second = int(((decimal_time - this_hour) * 60 - this_minute) * 60)
    return time(this_hour, this_minute, this_second)


# Loading files for packages and distances
file1 = FileLoader()
file2 = FileLoader()
list1 = file1.load_file(my_file='Distance Table.csv')
list2 = file2.load_file(my_file='Package File.csv')

# Creating and filling hash table with packages
my_hash_table = HashTable()
for item in list2:
    my_hash_table.insert_package(
        Package(int(item[0]), item[1], item[2], int(item[4]), item[5], int(item[6]), "At Hub", time(0, 0, 0)))

# Creating address list
address_list = list1[0][2:29]

for j in range(len(address_list)):
    for i, x in enumerate(address_list[j]):
        if x.isdigit():
            location = i
            multi_parts = address_list[j][i:].split(',')
            address_list[j] = multi_parts[0]
            break

# Creating distances list
distance_list = [[] for i in range(27)]
for i in range(1, 28):
    for j in range(2, 29):
        if list1[i][j] == '0':
            distance_list[i - 1].append(50)
        elif j > i:
            distance_list[i - 1].append(float(list1[j - 1][i + 1]))
        else:
            distance_list[i - 1].append(float(list1[i][j]))

# Truck objects
truck1 = Truck()
truck2 = Truck()

# Truck loads
load1 = [6, 25, 28, 32, 26, 1, 29, 7, 30, 8, 31, 40, 4]
load2 = [5, 37, 38, 13, 15, 19, 14, 16, 20, 39, 34, 21]
load3 = [3, 18, 36, 9, 2, 33, 27, 35, 10, 11, 12, 17, 22, 23, 24]

# Loading trucks
truck1.load_truck(load1)
truck2.load_truck(load2)
my_hash_table.search_hash_table(9).address = "410 S State St"  # Package 9 will not be delivered till after 10:20

# Nearest neighbor circuit algorithm
ordered_addresses1 = find_nearest(distance_list, address_list, truck1)
ordered_addresses2 = find_nearest(distance_list, address_list, truck2)

print("~~~~~~~~~~~~~~~~~~~~~~Truck Delivery~~~~~~~~~~~~~~~~~~~~~~")

# Distance variables initialized
total_distance = 0
distance_1 = 0
distance_2 = 0
distance_3 = 0

# Delivery time variables initialized
delivery_time_truck1 = 9.085
departure1_time = decimal_time_translation(delivery_time_truck1)  # Departure time for truck1

# Changing all packages status in first load to "En Route"
for package_id in load1:
    my_hash_table.search_hash_table(package_id).status = "En Route"

# Delivering first load
for address_index, min_distance in ordered_addresses1:
    distance_1 += min_distance
    delivery_time_truck1 += min_distance / 18
    for package_id in truck1.get_package_list():
        if my_hash_table.search_hash_table(package_id).address == address_list[address_index]:
            package = my_hash_table.search_hash_table(package_id)
            truck1.deliver(package, decimal_time_translation(delivery_time_truck1))

print(f"Truck 1 has finished and returned to hub at {decimal_time_translation(delivery_time_truck1)}")
print(f"Total distance of Truck 1 on route is {distance_1}")

# Delivery time variables initialized
delivery_time_truck2_first = 8.0
departure2_time = decimal_time_translation(delivery_time_truck2_first)

# Changing all packages status in second load to "En Route"
for package_id in load2:
    my_hash_table.search_hash_table(package_id).status = "En Route"

# Delivering second load
for address_index, min_distance in ordered_addresses2:
    distance_2 += min_distance
    delivery_time_truck2_first += min_distance / 18
    for package_id in truck2.get_package_list():
        if my_hash_table.search_hash_table(package_id).address == address_list[address_index]:
            package = my_hash_table.search_hash_table(package_id)
            truck2.deliver(package, decimal_time_translation(delivery_time_truck2_first))

print(f"Truck 2 has finished and returned to hub at {decimal_time_translation(delivery_time_truck2_first)}")
print(f"Total distance of Truck 2 on route is {distance_2}")

# Loading truck 2 again once its back at hub, and finding its delivery route
truck2.load_truck(load3)
ordered_addresses3 = find_nearest(distance_list, address_list, truck2)

# Delivery time variables initialized
delivery_time_truck2_second = delivery_time_truck2_first
departure3_time = decimal_time_translation(delivery_time_truck2_second)  # Departure time for truck3

# Changing all packages status in third load to "En Route"
for package_id in load3:
    my_hash_table.search_hash_table(package_id).status = "En Route"

# Delivering third load
for address_index, min_distance in ordered_addresses3:
    distance_3 += min_distance
    delivery_time_truck2_second += min_distance / 18
    for package_id in truck2.get_package_list():
        if my_hash_table.search_hash_table(package_id).address == address_list[address_index]:
            package = my_hash_table.search_hash_table(package_id)
            truck2.deliver(package, decimal_time_translation(delivery_time_truck2_second))

print(f"Truck 2 has finished and returned to hub at {decimal_time_translation(delivery_time_truck2_second)}")
print(f"Total distance of Truck 2 on route is {distance_3}\n")

# Computing total distance of all trucks
total_distance = distance_1 + distance_2 + distance_3
print(f"Total distance of all trucks is {total_distance}\n")

# Menu for user interface
while True:
    choice = ""
    while True:
        choice = int(input("Please select from the following:\n"
                           "1: Look up status of all packages at specific time\n"
                           "2: Look up specific package status at specific time\n"
                           "3: Exit program\n"))
        if choice in [1, 2, 3]:
            break

    match choice:
        # Status for all packages shown for specified time
        case 1:
            while True:
                # Getting user to input the time wanted for package check
                user_selected_time = input('Please select a time to check status of packages (ex: 13:30:00): ')
                try:
                    if len(user_selected_time) == 7:
                        hour = int(user_selected_time[0])
                        minute = int(user_selected_time[2:4])
                        second = int(user_selected_time[5:])
                    else:
                        hour = int(user_selected_time[0:2])
                        minute = int(user_selected_time[3:5])
                        second = int(user_selected_time[6:])
                    break
                except:
                    pass

            user_selected_time = time(hour, minute, second)

            # Correcting old address for user interface
            if user_selected_time < time(10, 20, 00):
                my_hash_table.search_hash_table(9).address = "300 State St"
            else:
                my_hash_table.search_hash_table(9).address = "410 S State St"

            delivery_status = ""

            # For each package id from 1 to 40, printing the package information for the user selected time
            for i in range(1, 41):
                current_package = my_hash_table.search_hash_table(i)

                # Defining departure time for truck of package
                if i in load1:
                    associated_departure = departure1_time
                elif i in load2:
                    associated_departure = departure2_time
                else:
                    associated_departure = departure3_time

                # Determining status of package
                if associated_departure <= user_selected_time < current_package.time:
                    delivery_status = "En Route"
                elif user_selected_time < associated_departure:
                    delivery_status = "At Hub"
                else:
                    delivery_status = f"Delivered at {current_package.time}"

                print(f"{current_package.special_str()} {delivery_status}")

            print("")

        # Status for individual package shown for specified time
        case 2:
            while True:
                # Getting user to input the time wanted for package check
                user_selected_time = input('Please select a time to check status of packages (ex: 13:30:00): ')
                try:
                    if len(user_selected_time) == 7:
                        hour = int(user_selected_time[0])
                        minute = int(user_selected_time[2:4])
                        second = int(user_selected_time[5:])
                    else:
                        hour = int(user_selected_time[0:2])
                        minute = int(user_selected_time[3:5])
                        second = int(user_selected_time[6:])
                    break
                except:
                    pass

            user_selected_time = time(hour, minute, second)

            # Correcting old address for user interface
            if user_selected_time < time(10, 20, 00):
                my_hash_table.search_hash_table(9).address = "300 State St"
            else:
                my_hash_table.search_hash_table(9).address = "410 S State St"

            user_selected_id = int(input('Please select a package id (1-40): '))

            current_package = my_hash_table.search_hash_table(user_selected_id)

            # Defining departure time for truck of package
            if user_selected_id in load1:
                associated_departure = departure1_time
            elif user_selected_id in load2:
                associated_departure = departure2_time
            else:
                associated_departure = departure3_time

                # Determining status of package
            if associated_departure <= user_selected_time < current_package.time:
                delivery_status = "En Route"
            elif user_selected_time < associated_departure:
                delivery_status = "At Hub"
            else:
                delivery_status = f"Delivered at {current_package.time}"

            print(f"{current_package.special_str()} {delivery_status}\n")

        # Exit of program
        case 3:
            exit()
