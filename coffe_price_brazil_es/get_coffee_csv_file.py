import pandas as pd
from bs4 import BeautifulSoup
import requests
import locale
from locale import atof
locale.setlocale(locale.LC_NUMERIC, 'en_DK.utf8')


def get_csv_file():
    """ Cria um arquivo csv com as informações sobre o preço do café

    :return: Dataframe com preços e Informações sobre o café
    :rtype: pd.Dataframe e pd.Series
    """
    page_url = "https://www.cecafe.com.br/indicadores-de-mercado/precos-vitoria/"
    html = requests.get(page_url)

    soup = BeautifulSoup(html.content, "html.parser")

    tbl = soup.find("table")

    body = tbl.find_all("tr")

    body_rows = body[1:]

    headings = ["DATA", "ARABICA RUIM", "ARABICA BOM", "CONILLON"]

    all_rows = []
    for row_num in range(len(body_rows)):
        row = []
        for row_item in body_rows[row_num].find_all("td"):

            info = row_item.text

            row.append(info)

        all_rows.append(row)

    df = pd.DataFrame(data=all_rows, columns=headings)

    # Ultima linha é de informação dos grãos, self.info guarda informação dos grãos
    dfInfo = df.iloc[-1]

    # Retira a ultima linha da tabela
    df = df[:-1]

    # Transforma a coluna de data como a de index
    df.set_index("DATA", inplace=True)

    df = df.applymap(atof)

    # Tira a "tail" do dataframe
    df.to_csv("price_table.csv", index=False)

    return df, dfInfo
