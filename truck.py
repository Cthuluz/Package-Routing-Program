class Truck:
    """
        Truck class holds every package id in a list for that specific truck
        Functions include:
        1. load_truck: loads the truck with all inputted package ids
        2. deliver: delivers a package, changing the status of that package to "Delivered" and
        recording the delivered time to the package time attribute
        3. get_package_list: returns a list of all packages within the truck
        """

    # Truck constructor, initializing the package id list
    def __init__(self):
        self.loaded_packages = []

    # Loads the truck with a package, adding it to the list
    def load_truck(self, packages):
        self.loaded_packages = packages

    # Delivers a package, changing the status of that package to "Delivered"
    # Records the delivery time to the package time attribute
    def deliver(self, package, time):
        package.time = time
        package.status = "Delivered"

    # Returns a list of all packages within the truck
    def get_package_list(self) -> list:
        return self.loaded_packages
