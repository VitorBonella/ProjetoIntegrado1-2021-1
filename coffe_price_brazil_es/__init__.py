from coffee import Coffee

coffee = Coffee()
#print(coffee.get_table()["ARABICA RUIM"])
#print(coffee.get_price("CONILLON", recent=True))
print(coffee.get_prices_by_year(2000))

