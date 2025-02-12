from data_worker import min_distance_from, get_distance
from datetime import timedelta

from deliveryStatuses import DeliveryStatus


class Truck:
    def __init__(self, capacity=16, speed=18, load=0, packages=None, mileage=0, address="HUB", depart_time=None):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages if packages else []
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time
        self.undelivered = []



    # Method for ordering packages on a given truck using the nearest neighbor algo
    # This method also calculates the distance a given truck drives once the packages are sorted
    def delivering_packages(self, package_table, delivery_status_structure):
        #place all packages using packageID into undelivered array
        for packageID in self.packages:
            package = package_table.get(packageID)
            if (packageID == 9):
                package.address = '410 S State St'
                package.zip = "84111"
            package.status = 'en route'
            self.undelivered.append(package)
        # clear packages so that they can be rearranged in the truck in  the order of the nearest neighbor
        self.packages.clear()

        #  loops through list of undelivered
        #adds the nearest package into the packages list
        while len(self.undelivered) > 0:
            next_package, next_address = min_distance_from(self.address, self.undelivered)
            # adds the neares pkg to the packages list
            self.packages.append(next_package.package_id)
            # Removes the same package from the undelivered list
            self.undelivered.remove(next_package)
            # Takes the mileage driven to this packaged into the mileage attribute
            self.mileage += next_address
            # Updates truck's current address attribute to the package it drove to
            self.address = next_package.address
            # Updates the time it took for the truck to drive to the nearest package
            self.time += timedelta(hours=next_address / self.speed)
            next_package.delivery_time = self.time
            next_package.departure_time = self.depart_time
            next_package.status = 'Delivered'
            delivery_status_structure.add_current_statuses(package_table, self.time)


    def __str__(self):
        return f"Truck({self.capacity} cap, {self.load} loaded, {self.mileage} miles, @ {self.address})"