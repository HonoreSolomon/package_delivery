# Author: Honore Solomon
# Student ID: 011865887
# Title: C950 WGUPS ROUTING PROGRAM
import datetime
from HashTable import HashTable
# from Package import Package
from data_worker import *
from truck import Truck


#initialize data
load_address_data()
load_distance_data()

#instatiate hash table
package_hash_table = HashTable()
#loads packages into hash table
store_packages(package_hash_table)
#create truck object truck 1
truck1 = Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

# Create truck object truck2
truck2 = Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 3], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Create truck object truck3
truck3 = Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))
#runs truck delivery method
truck1.delivering_packages(package_hash_table)
truck2.delivering_packages(package_hash_table)
#ensures truck 3 will not depart until the first of the first two trucks finish
truck3.depart_time = min(truck1.time,truck2.time)
truck3.delivering_packages(package_hash_table)



print(truck1.mileage + truck2.mileage + truck3.mileage)

package_hash_table.print()










