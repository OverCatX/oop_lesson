import copy
import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(r)

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(r)


class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        self.table_database.append(table)

    def search(self, table_name):
        for table in self.table_database:
            if table.table_name == table_name:
                return table
        return None


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def aggregate(self, aggregation_function, aggregation_key):
        temps = []
        for item1 in self.table:
            temps.append(float(item1[aggregation_key]))
        return aggregation_function(temps)

    def __str__(self):
        return self.table_name + ':' + str(self.table)


table_cities = Table('cities', cities)
table_countries = Table('countries', countries)
table_db = TableDB()
table_db.insert(table_cities)
table_db.insert(table_countries)
my_table1 = table_db.search('cities')
my_table2 = table_db.search('countries')
table_cities_filtered_italy = my_table1.filter(lambda x: x['country'] == 'Italy')
table_cities_filtered_sweden = my_table1.filter(lambda x: x['country'] == 'Sweden')
print('Average Temperature for all the cities in Italy')
print(table_cities_filtered_italy.aggregate(lambda x: sum(x) / len(x), 'temperature'))
print('')
print('Average Temperature for all the cities in Sweden')
print(table_cities_filtered_sweden.aggregate(lambda x: sum(x) / len(x), 'temperature'))
print('')
print('Min temperature for all the cities in Italy')
print(table_cities_filtered_italy.aggregate(lambda x: min(x), 'temperature'))
print('')
print('Max temperature for all the cities in Sweden')
print(table_cities_filtered_sweden.aggregate(lambda x: max(x), 'temperature'))
print('')

table3 = my_table2.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print('Min-Max temperature for cities in EU dont have coastlines')
print('')
for tables in table3.table:
    table4 = my_table1.filter(lambda x: x['country'] == tables['country'])
    print(f'Min temperature in {tables['country']}')
    print(table4.aggregate(lambda x: min(x), 'temperature'))
    print(f'Max temperature in {tables['country']}')
    print(table4.aggregate(lambda x: max(x), 'temperature'))
    print('')


for tables in my_table1.table:
    table5 = my_table1.filter(lambda x: x['country'] == tables['country'])
    print(f'Min latitude in {tables['country']}')
    print(table5.aggregate(lambda x: min(x), 'latitude'))
    print(f'Max latitude in {tables['country']}')
    print(table5.aggregate(lambda x: max(x), 'latitude'))
    print('')
