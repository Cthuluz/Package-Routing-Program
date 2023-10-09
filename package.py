class Package:
    """
    Package class holds each package and their individual attributes
    Functions include:
    1. __str__: definition of the string version of an object
    2. special_str: a string that contains all attributes to print nicely
    """

    # Constructor of package class, initializing all attributes
    def __init__(self, package_id, address, city, zipcode, deadline, weight, status, time):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.time = time

    # String definition as the id for created objects
    def __str__(self):
        return str(self.package_id)

    # A special string
    def special_str(self):
        return str(f"Id: {self.package_id} || Address: {self.address} || City: {self.city} || Zipcode: {self.zipcode} || Deadline: {self.deadline} || Weight: {self.weight} || ")

