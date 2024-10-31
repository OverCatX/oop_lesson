import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class DataProcess:

    def __init__(self):
        self.cities = []
        self.countries = []
        self.filtered_list = []

    def cities_init(self):
        with open(os.path.join(__location__, 'Cities.csv')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.cities.append(dict(r))

    def countries_init(self):
        with open(os.path.join(__location__, 'Countries.csv')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.countries.append(dict(r))

    # Print the average temperature of all the cities
    def average_temp_cities(self):
        print("The average temperature of all the cities:")
        temps = []
        for city in self.cities:
            temps.append(float(city['temperature']))
        print(sum(temps) / len(temps))
        print()

    # Print all cities
    def search_all_cities_in_country(self, country):
        cities_temp = []
        for city in self.cities:
            if city['country'] == country:
                cities_temp.append(city['city'])
        print("All the cities in", country, ":")
        print(cities_temp)
        print()

    # Print the average temperature for all the cities
    def search_average_temp_cities(self, country):
        temps = []
        for city in self.cities:
            if city['country'] == country:
                temps.append(float(city['temperature']))
        print("The average temperature of all the cities in", country, ":")
        print(sum(temps) / len(temps))
        print()

    # Print the max temperature for all the cities
    def search_max_temp_in_cities(self, country):
        temps = []
        for city in self.cities:
            if city['country'] == country:
                temps.append(float(city['temperature']))
        print("The max temperature of all the cities in", country, ":")
        print(max(temps))
        print()

    # Print the min temperature for all the cities
    def search_min_temp_in_cities(self, country):
        temps = []
        for city in self.cities:
            if city['country'] == country:
                temps.append(float(city['temperature']))
        print("The min temperature of all the cities in", country, ":")
        print(min(temps))
        print()

    def search_min_latitude_in_cities(self, country):
        latitude = []
        for city in self.cities:
            if city['country'] == country:
                latitude.append(float(city['latitude']))
        print("The min latitude of all the cities in", country, ":")
        print(min(latitude))
        print()

    def search_max_latitude_in_cities(self, country):
        latitude = []
        for city in self.cities:
            if city['country'] == country:
                latitude.append(float(city['latitude']))
        print("The max latitude of all the cities in", country, ":")
        print(max(latitude))
        print()

    # Let's write a function to filter out only items that meet the condition
    # Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
    def filter(self, condition, dict_list):
        for item in dict_list:
            if condition(item):
                self.filtered_list.append(item)
        return self.filtered_list

    def search_all_latitude(self):
        x = filter(lambda x: float(x['latitude']) >= 60.0, self.cities)
        for item in x:
            print(item)

    def search_cities_with_coastline(self, eu_check, coastline_check):
        cc = []
        for countries in self.countries:
            if eu_check == 'all' and coastline_check == 'all':
                cc.append(countries['country'])
            if countries['EU'] == eu_check and countries['coastline'] == coastline_check:
                cc.append(countries['country'])
        return cc

    # Let's write a function to do aggregation given an aggregation function and an aggregation key
    def aggregate(self, aggregation_key, aggregation_function, dict_list):
        v = [d[aggregation_key] for d in dict_list if aggregation_key in dict_list]
        return aggregation_function[v]


# Let's write code to
# - print the average temperature for all the cities in Italy
# - print the average temperature for all the cities in Sweden
# - print the min temperature for all the cities in Italy
# - print the max temperature for all the cities in Sweden
dataprocessing = DataProcess()
dataprocessing.cities_init()
dataprocessing.countries_init()
dataprocessing.search_all_cities_in_country('Italy')
dataprocessing.search_all_cities_in_country('Sweden')
dataprocessing.search_min_temp_in_cities('Italy')
dataprocessing.search_max_temp_in_cities('Sweden')
for country in dataprocessing.search_cities_with_coastline('yes', 'no'):
    dataprocessing.search_min_temp_in_cities(country)
for country in dataprocessing.search_cities_with_coastline('yes', 'no'):
    dataprocessing.search_max_temp_in_cities(country)
for country in dataprocessing.search_cities_with_coastline('all', 'all'):
    dataprocessing.search_min_latitude_in_cities(country)
for country in dataprocessing.search_cities_with_coastline('all', 'all'):
    dataprocessing.search_max_latitude_in_cities(country)