class Solution(object):
    def destCity(self, paths):
        
        # Create a set to store all starting cities
        starting_cities = set()

        # Iterate through the paths to find starting and destination cities
        for path in paths:
            starting_cities.add(path[0])

        # Iterate through the paths to find the destination city
        for path in paths:
            destination_city = path[1]
            if destination_city not in starting_cities:
                return destination_city
    