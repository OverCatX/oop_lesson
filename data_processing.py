import csv, os

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
        _index = self.search(table.table_name)
        if _index == -1:
            self.table_database.append(table)
        else:
            print(table, "Duplicated table")

    def search(self, table_name):
        for i in range(len(self.table_database)):
            if self.table_database[i].table_name == table_name:
                return i
        return -1


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        filtered_list = []
        for item1 in self.table:
            if condition(item1):
                filtered_list.append(item1)
        return filtered_list

    def aggregate(self, aggregation_function, aggregation_key):
        temps = []
        for _item in self.table:
            temps = [].append(float(_item[aggregation_key]))
        return aggregation_function(temps)

    def __str__(self):
        return self.table_name + ':' + str(self.table)

# Let's write code to
# - print the average temperature for all the cities in Italy
# - print the average temperature for all the cities in Sweden
# - print the min temperature for all the cities in Italy
# - print the max temperature for all the cities in Sweden
