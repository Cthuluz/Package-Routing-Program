class HashTable:
    """
            HashTable class holds a self adjusting list of packages
            Functions include:
            1. insert_package: inserts the inputted package into the correct spot within the list determined by the hash
            function
            2. search_hash_table: searches the hash table using the modulo hash function and linear probing
            """

    # Constructor for hash table, initializing the list and filling it with 40 empty slots
    def __init__(self):
        self.hashList = []

        for i in range(40):
            self.hashList.append([])

    # Inserts the inputted package into the correct spot within the list determined by the hash function
    def insert_package(self, new_package):
        # Initializing hash number determined by modulo hash function
        hash_number = new_package.package_id % len(self.hashList)
        increment_number = 0

        # Finding empty spot to place package
        while increment_number < len(self.hashList):
            if not self.hashList[hash_number]:
                self.hashList[hash_number] = new_package
                return
            else:
                increment_number += 1
                hash_number = (hash_number + 1) % len(self.hashList)

        # If no spots are found, the package is inserted at the original hash number location, moving all other packages
        # above up one
        self.hashList.insert(new_package.package_id % len(self.hashList), new_package)

    # Searches the hash table using the modulo hash function and linear probing
    def search_hash_table(self, key):
        # Initializing the hash number from the modulo hash function
        hash_number = key % len(self.hashList)
        increment_number = 0

        # Searching for the package at the hash number location
        # Using linear probing if package is not found at first
        while increment_number < len(self.hashList):
            if str(self.hashList[hash_number]) == str(key):
                return self.hashList[hash_number]

            hash_number = (hash_number + 1) % len(self.hashList)
            increment_number += 1

        print("No package found")
