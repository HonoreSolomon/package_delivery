# Hash Table class
#used some styles from the 1st hash table webinar
class HashTable:
    #constructor that has an optional capacity or default of 10.
    #Assigns an empty list to every bucket
    def __init__(self):
        #initialize table with a list
        self.size = 6
        self.table = [None] * self.size
    # function to handle hashing of key
    def _get_hash(self, key):
        # hashed = 0
        # for char in key:
        #     hashed += ord(char)
        return  hash(key) % len(self.table)

    # searches the bucketlist for the given key  and return the Key value pair
    def __getKV(self, key):
        key_hash = self._get_hash(key)
        bucket_list = self.table[key_hash]
        #loop over all key values in bucketlist and return the matching key_value
        if bucket_list is not None:
            for kv in bucket_list:
                if kv[0] == key:
                    return kv
        return None



    # #function to resize the list if needed
    # def __resize_if_needed__(self):
    #     # factor of items / size of list
    #     resize_factor = self.size / len(self.table)
    #     #if size is larger than the factor we will double the list size by looping through and adding lists
    #     if self.size > resize_factor:
    #         for i in range(len(self.table)):
    #             self.table.append([])



    #inserts a kv pair into the hashed bucket and updates if key is already there
    def insert(self, key, value):
        #uses the private hash func to return the bucket
        # self.__resize_if_needed__()

        key_hash = self._get_hash(key)
        bucket_list = self.table[key_hash]
        key_value = [key, value]
        #checks if the current bucket has a list, if not instantiates a list with the kv and returns true
        if bucket_list is None:
            self.table[key_hash] = list([key_value])
            return True
        # checks if the key is already in the bucket list if yes, the it updates the value and returns true
        else:
            for kv in bucket_list:
                if kv[0] == key:
                    kv[1] = value
                    return True
        #if not adds the kv pair to the end of the list
            bucket_list.append(key_value)
            return True


    def get(self, key):
        kv_pair = self.__getKV(key)
        return kv_pair[1]
    #
    def remove(self, key):
        bucket = self._get_hash(key)
        bucket_list = self.table[bucket];
        if bucket_list is not None:
            key_value = self.__getKV(key)
            bucket_list.remove(key_value)

        # self.size = self.size - 1

    def print(self):
        for bucket in self.table:
            if bucket is not None:
                for package in bucket:
                    print(package[1])


