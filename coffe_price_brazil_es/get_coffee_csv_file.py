import pandas as pd
from bs4 import BeautifulSoup
import requests


def get_csv_file():
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

    # Transforma a coluna de data como a de index
    df.set_index("DATA", inplace=True)

    # Tira a "tail" do dataframe
    df.to_csv("price_table.csv", index=False)

    return df
