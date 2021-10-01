from app import app
from flask import render_template
from coffe_price_brazil_es import coffee


@app.route("/infocafe/geral")
def graph_geral():

    # labels, values0, values1, values2 = coffee.get_prices_by_range("05/05/2020", "01/01/2022")
    # labels, values0, values1, values2 = coffee.get_prices_by_year(2019)

    labels, values0 = coffee.get_prices_by_type("ARABICA RUIM")
    _, values1 = coffee.get_prices_by_type("ARABICA BOM")
    _, values2 = coffee.get_prices_by_type("CONILLON")
    values = [values0, values1, values2]
    last_prices = [round(values0[-1]), round(values1[-1]), round(values2[-1])]

    delta_price = [True if values0[-1] > values0[-2] else False,
                   True if values1[-1] > values1[-2] else False,
                   True if values2[-1] > values2[-2] else False]

    prices_mean = [round((values0[-8:-1].sum())/7), round((values1[-8:-1].sum())/7), round((values2[-8:-1].sum())/7)]

    return render_template("graph.html",
                           labels=labels,
                           values=values,
                           last_prices=last_prices,
                           delta_price=delta_price,
                           prices_mean=prices_mean,
                           types=["Arabica Dura", "Arabica Rio", "Conillon"], colors=["rgb(0,220,255)", "rgb(0,50,255)", "rgb(63,255,0)"])

'''
@app.route("/infocafe/arabica_ruim")
def graph_arabica_ruim():

    # labels, values0, values1, values2 = coffee.get_prices_by_range("05/05/2020", "01/01/2022")
    # labels, values0, values1, values2 = coffee.get_prices_by_year(2019)

    labels, values0 = coffee.get_prices_by_type("ARABICA RUIM")
    values = [values0]
    return render_template("graph.html", labels=labels, values=values, types=["Arabica ruim"], colors=["rgb(0,220,255)"])


@app.route("/infocafe/arabica_bom")
def graph_arabica_bom():

    # labels, values0, values1, values2 = coffee.get_prices_by_range("05/05/2020", "01/01/2022")
    # labels, values0, values1, values2 = coffee.get_prices_by_year(2019)

    labels, values0 = coffee.get_prices_by_type("ARABICA BOM")
    values = [values0]
    return render_template("graph.html", labels=labels, values=values, types=["Arabica bom"], colors=["rgb(0,50,255)"])


@app.route("/infocafe/conillon")
def graph_conillon():

    # labels, values0, values1, values2 = coffee.get_prices_by_range("05/05/2020", "01/01/2022")
    # labels, values0, values1, values2 = coffee.get_prices_by_year(2019)

    labels, values0 = coffee.get_prices_by_type("CONILLON")
    values = [values0]
    return render_template("graph.html", labels=labels, values=values, types=["Conillon"], colors=["rgb(63,255,0)"])
'''