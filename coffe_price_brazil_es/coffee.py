from coffe_price_brazil_es.get_coffee_csv_file import get_csv_file
import pandas as pd

class Coffee:
    def __init__(self):
        try:
            self.table, self.info = get_csv_file()
        except AttributeError:
            print("CSV COFFEE FILES ARE OFFLINE")

    def update_prices(self, table):
        self.table = get_csv_file()

    def get_table(self):
        return self.table

    # Type vai de "ARABICA RUIM","ARABICA BOM", "CONILL
    def get_prices_by_type(self, coffee_type):
        try:
            return self.table[coffee_type].index, self.table[coffee_type].values
        except KeyError:
            print("Type {} doesn't exist. Allowed types are: {}, {} and {}".format(coffee_type, self.table.columns[0], self.table.columns[1], self.table.columns[2]))
            return None

    def get_prices_by_range(self, start, end, coffee_type=None):

        datetime_data = pd.to_datetime(self.table.index, format="%d/%m/%Y")

        mask = (datetime_data > start) & (datetime_data <= end)

        data = self.table.loc[mask]

        if(coffee_type == None):
            return data.iloc[:, 0].index, data.iloc[:, 0].values, data.iloc[:, 1].values, data.iloc[:, 2].values
        else:
            return data[coffee_type].index, data[coffee_type].values

    def get_prices_by_year(self, year, coffee_type=None):
        data = self.table[self.table.index.str.contains(str(year))]
        if(coffee_type == None):
            return data.iloc[:, 0].index, data.iloc[:, 0].values, data.iloc[:, 1].values, data.iloc[:, 2].values
        else:
            coffee_type = str(coffee_type)
            return data[coffee_type].index, data[coffee_type].values

    # Função que printa os tipos de grãos na tabela
    def print_info(self):
        for grao_info in self.info:
            print(grao_info)

    def get_price(self, coffee_type, day=None, recent=False):
        if recent:
            try:
                return self.table[coffee_type].iloc[-1]
            except KeyError:
                print("Type {} doesn't exist. Allowed types are: {}, {} and {}".format(coffee_type, self.table.columns[0], self.table.columns[1], self.table.columns[2]))
                return None
        else:
            try:
                return self.table.loc[day, coffee_type]
            except KeyError:
                if coffee_type not in self.table.columns:
                    print("Type {} doesn't exist. Allowed types are: {}, {} and {}".format(coffee_type, self.table.columns[0], self.table.columns[1], self.table.columns[2]))
                else:
                    print("Day {} not in the Price Table.".format(day))
                return None
