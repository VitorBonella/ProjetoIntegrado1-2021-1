from get_coffe_csv_file import get_csv_file


class Coffe:
    def __init__(self):
        self.table = get_csv_file()

    def update_prices(self, table):
        self.table = get_csv_file()

    def get_table(self):
        return self.table

    # Type vai de "ARABICA RUIM","ARABICA BOM", "CONILL
    def get_pricesby_type(self, coffe_type):
        return self.table.loc[coffe_type]

    def get_price(self, coffe_type, day):
        return self.table.loc[day, coffe_type]
