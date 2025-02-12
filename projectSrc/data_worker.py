import csv
from Package import Package

# ---------- Global Data Structures ----------
distance_data = []  # 2D list for distance matrix
address_data = []    # List of address strings
address_index = {}  # Dictionary for O(1) address lookups

# ---------- Package Loading ----------
def store_packages(table):
    #reads the CSV of package file
    file = "projectSrc/CSV/WGUPS Package File(Sheet1).csv"
    with open(file) as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        next(reader, None)
        #creates package objects for each package and adds them to the hashtable with the package id as key
        for row in reader:
            # #create package from file data
            package = Package(*row[:8])
            #insert data
            table.insert(package.package_id, package)

# Distance Data Loading
def load_distance_data():
    global distance_data
    file = "projectSrc/CSV/Distance_File.csv"
    with open(file) as fp:
        #uses list comprehension to store distance data
        distance_data = [row for row in csv.reader(fp)]

#address data loading
def load_address_data():
    global address_data, address_index
    file = "projectSrc/CSV/Address_File.csv"
    with open(file) as fp:
        #uses list comprehension to create grab the address data from the csv and creates a dict to access address by index
        address_data = [row[2] for row in csv.reader(fp)]
        address_index = {address: index for index, address in enumerate(address_data)}

#distance calculation
#find the distance between two addresses
def get_distance(address1, address2):
    #grabs index for addresses from dict
    i = address_index[address1]
    j = address_index[address2]
    distance = distance_data[i][j]
    if distance == '':
        distance = distance_data[j][i]
    #returns the difference as a float by using the max as the first index and themin as the second.
    return float(distance)


#nearest neighbor algorithim
def min_distance_from(from_address, packages):
    #validate input address
    if from_address not in address_index:
        raise ValueError(f"Address {from_address} is not in database")

    next_address = 2000
    next_package = None
    #iterate through all packages to find the nearest package O(n)
    for package in packages:
        #uses premade method to get distance calc

        if package.package_id in [25,6]:
            next_package = package
            next_address = get_distance(from_address, package.address)
            return  next_package, next_address
        if get_distance(from_address, package.address) <= next_address:
            next_address = get_distance(from_address, package.address)
            next_package = package
        # distance = get_distance(from_address, package.address)
        # if distance < next_address:
        #     next_address, next_package = distance, package
    return  next_package, next_address

