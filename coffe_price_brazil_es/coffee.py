from coffe_price_brazil_es.get_coffee_csv_file import get_csv_file
import pandas as pd
class Coffee:
    def __init__(self):
        try:
            self.table, self.info = get_csv_file()
        except AttributeError:
            print("CSV COFFEE FILES ARE OFFLINE")

    def update_prices(self, table):
        """ Atualiza a tabela de preços

        Essa função atualiza a tabela de preços mediante o acesso do usuário;

        :param table: Tabela de preços
        :type table: Matrix
        :return:
        :rtype:
        """
        self.table = get_csv_file()

    def get_table(self):
        """ Retorna a tabela de preços

        :return: Tabela de preços
        :rtype: Matrix
        """
        return self.table

    # Type vai de "ARABICA RUIM","ARABICA BOM", "CONILLON"
    def get_prices_by_type(self, coffee_type):
        """ Retorna um vetor com os preços de um tipo de café específico

        :param coffee_type: Um tipo de café
        :type coffee_type: ["ARABICA RUIM","ARABICA BOM", "CONILLON"]
        :return: Valores de um tipo de café específico
        :rtype: Vetor de valores de um tipo específico
        """
        try:
            return self.table[coffee_type].index, self.table[coffee_type].values
        except KeyError:
            print("Type {} doesn't exist. Allowed types are: {}, {} and {}".format(coffee_type, self.table.columns[0], self.table.columns[1], self.table.columns[2]))
            return None

    def get_prices_by_range(self, start, end, coffee_type=None):
        """ Valores do preço do café em um determinado periodo, se coffee_type for passado, retorna os valores de um único tipo de café em um período;

        :param start: Dia inicial
        :type start: String
        :param end: Dia final
        :type end: String
        :param coffee_type: Tipos de café
        :type coffee_type: ["ARABICA RUIM","ARABICA BOM", "CONILLON"]
        :return: Vetor com preços da sacas em determinado periodo
        :rtype: Vetor
        """
        datetime_data = pd.to_datetime(self.table.index, format="%d/%m/%Y")

        mask = (datetime_data > start) & (datetime_data <= end)

        data = self.table.loc[mask]

        if(coffee_type == None):
            return data.iloc[:, 0].index, data.iloc[:, 0].values, data.iloc[:, 1].values, data.iloc[:, 2].values
        else:
            return data[coffee_type].index, data[coffee_type].values

    def get_prices_by_year(self, year, coffee_type=None):
        """ Valores do preço do café em um determinado ano, se coffee_type for passado, retorna os valores de um único tipo de café em um ano;

        :param year: Ano
        :type year: String
        :param coffee_type: Tipo de café
        :type coffee_type: ["ARABICA RUIM","ARABICA BOM", "CONILLON"]
        :return: Retorna a tabela de preços de um ano específico
        :rtype: Vetor
        """
        data = self.table[self.table.index.str.contains(str(year))]
        if(coffee_type == None):
            return data.iloc[:, 0].index, data.iloc[:, 0].values, data.iloc[:, 1].values, data.iloc[:, 2].values
        else:
            coffee_type = str(coffee_type)
            return data[coffee_type].index, data[coffee_type].values

    # Função que printa os tipos de grãos na tabela
    def print_info(self):
        """ Mostra as informações sobre cada tipo de café

        :return: None
        :rtype: None
        """
        for grao_info in self.info:
            print(grao_info)

    def get_price(self, coffee_type, day=None, recent=False):
        """ Retorna o ultimo preço de um determinado dia, se recent for passado retorna o ultimo dia de coleta;

        :param coffee_type: Tipo de café
        :type coffee_type: ["ARABICA RUIM","ARABICA BOM", "CONILLON"]
        :param day: Dia
        :type day: String
        :param recent: Preço atual
        :type recent: Boolean
        :return: Preço de um tipo de café em um determinado dia
        :rtype: Float
        """
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
