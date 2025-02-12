# Author: Honore Solomon
# Student ID: 011865887
# Title: C950 WGUPS ROUTING PROGRAM
import datetime
from pprint import pprint

from HashTable import HashTable
# from Package import Package
from data_worker import *
from deliveryStatuses import DeliveryStatus
from truck import Truck


#initialize data
load_address_data()
load_distance_data()

delivery_status_structure = DeliveryStatus()



#instatiate hash table
package_hash_table = HashTable()
#loads packages into hash table
store_packages(package_hash_table)

#create truck object truck 1
truck1 = Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))
#  3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39
# Create truck object truck2
truck2 = Truck(16, 18, None, [3, 6, 18, 25, 27, 28, 32, 33, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
# 2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33
# Create truck object truck3
truck3 = Truck(16, 18, None, [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22, 23, 24, 26], 0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
#runs truck delivery method
truck1.delivering_packages(package_hash_table,delivery_status_structure)

truck2.delivering_packages(package_hash_table,delivery_status_structure)


#ensures truck 3 will not depart until the first of the first two trucks finish
truck3.depart_time = min(truck1.time,truck2.time)
truck3.delivering_packages(package_hash_table,delivery_status_structure)



class Main:
    #User Interface for package delivery status
    # the following will be printed upon running the programj
    print("Welcome to WGUPS")
    # Prints packages showing all were delivered
    for packageID in range(1, 41):
        package = package_hash_table.get(packageID)
        print(str(package))
    #print the total mileage for all trucks
    print(f"The total Mileage for the route is: {truck1.mileage + truck2.mileage + truck3.mileage}")
    while True:
        #the menu for the package statuses will appear
        print("Please select one of the options below:")
        print("*" * 10)
        print(" " * 10)
        print("1. Print All Package Status and Total Mileage ")
        print(" " * 10)
        print("2. Get a Single Package Status with a Time " )
        print(" " * 10)
        print("3. Get All Package Status with a Time ")
        print(" " * 10)
        print("4. Exit the Program ")
        print(" " *10)
        print("*" * 10)
        choice = input()
        if choice == "1":
            for time, packages in delivery_status_structure.map.items():
                print(f"Time: {time}: Package Status:{packages}")
            print(f"Total Mileage is {truck1.mileage + truck2.mileage + truck3.mileage}")
        elif choice == "2":
            user_time = input("Please enter a time to check status of package. Use the following format, HH:MM:SS")
            (h, m, s) = user_time.split(":")
            convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            chosen_package = int(input("Please enter a package ID: "))
            time_stamp_dict, time_stamp = delivery_status_structure.get_time_stamp(convert_timedelta)
            package_status = time_stamp_dict.get(chosen_package)
            print(f"Package ID: {chosen_package} Time: {str(time_stamp)}: Package Status:{package_status}")
        elif choice == "3":
            user_time = input("Please enter a time to check status of package. Use the following format, HH:MM:SS")
            (h, m, s) = user_time.split(":")
            convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            time_stamp_dict, time_stamp = delivery_status_structure.get_time_stamp(convert_timedelta)
            print(f"Chosen Time: {convert_timedelta} Last Packages Delivered at {time_stamp}")
            for id, packages in time_stamp_dict.items():
                print(f"Package: {id}: Package Status:{packages}")

        elif choice == "4":
            exit()








