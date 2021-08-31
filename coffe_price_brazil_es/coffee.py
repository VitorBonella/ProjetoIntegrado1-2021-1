from get_coffee_csv_file import get_csv_file


class Coffee:
    def __init__(self):
        try:
            self.table = get_csv_file()

            # Ultima linha é de informação dos grãos, self.info guarda informação dos grãos
            self.info = self.table.iloc[-1]

            # Retira a ultima linha da tabela
            self.table = self.table[:-1]
        except AttributeError:
            print("CSV COFFEE FILES ARE OFFLINE")

    def update_prices(self, table):
        self.table = get_csv_file()

    def get_table(self):
        return self.table

    # Type vai de "ARABICA RUIM","ARABICA BOM", "CONILL
    def get_prices_by_type(self, coffee_type):
        try:
            return self.table[coffee_type]
        except KeyError:
            print("Type {} doesn't exist. Allowed types are: {}, {} and {}".format(coffee_type, self.table.columns[0], self.table.columns[1], self.table.columns[2]))
            return None

    # Função que printa os tipos de grãos na tabela
    def print_info(self):
        for grao_info in self.info:
            print(grao_info)

    def get_price(self, coffee_type, day=None, recent=False):
        if(recent == True):
            try:
                return self.table[coffee_type].iloc[-1]
            except KeyError:
                print("Type {} doesn't exist. Allowed types are: {}, {} and {}".format(coffee_type, self.table.columns[0], self.table.columns[1], self.table.columns[2]))
                return None
        else:
            try:
                return self.table.loc[day, coffee_type]
            except KeyError:
                if(coffee_type not in self.table.columns):
                    print("Type {} doesn't exist. Allowed types are: {}, {} and {}".format(coffee_type, self.table.columns[0], self.table.columns[1], self.table.columns[2]))
                else:
                    print("Day {} not in the Price Table.".format(day))
                return None
