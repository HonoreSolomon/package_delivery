from data_worker import min_distance_from, get_distance
from datetime import timedelta

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
    def delivering_packages(self, package_table):
        #place all packages using packageID into undelivered array
        for packageID in self.packages:
            package = package_table.get(packageID)
            self.undelivered.append(package)
        # clear packages so that they can be rearranged in the truck in  the order of the nearest neighbor
        self.packages.clear()

        #  loops through list of undelivered
        #adds the nearest package into the packages list
        for package in self.undelivered:
            nearest_pkg, distance = min_distance_from(self.address, self.undelivered)
            # adds the neares pkg to the packages list
            self.packages.append(nearest_pkg.package_id)
            # Removes the same package from the undelivered list
            self.undelivered.remove(nearest_pkg)
            # Takes the mileage driven to this packaged into the mileage attribute
            self.mileage += distance
            # Updates truck's current address attribute to the package it drove to
            self.address = nearest_pkg.address
            # Updates the time it took for the truck to drive to the nearest package
            self.time += timedelta(hours=distance / 18)
            nearest_pkg.delivery_time = self.time
            nearest_pkg.departure_time = self.depart_time
            nearest_pkg.upd

    def __str__(self):
        return f"Truck({self.capacity} cap, {self.load} loaded, {self.mileage} miles, @ {self.address})"