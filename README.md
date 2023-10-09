# Package Routing Program

This package routing program uses a hashmap to store all package objects and a nearest neighor algorithm for efficient delivery. Package and delivery address information is imported using excel files. There are two different delivery trucks and each is able to hold up to 16 packages at a time, while to total number of packages to be delivered is 40. Each package may have a time limit and special instructions noted in the package excel file.

There is a package class to hold all information about each individual package, as well as a truck class to hold a list of all the package ids of each truck load. A hashtable class is also incorporated, allowing a hash table object to be created to store all 40 package objects. This hash table has an insert and search function, both of which use a modulo hash function for object location within the hashtable.

The user interface simply uses the console, showing when each truck has finished and its total distance. The user can look up the status of all packages at a specific time, a specific package at a specific time or exit the program.
