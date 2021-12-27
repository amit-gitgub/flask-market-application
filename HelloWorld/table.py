from tabulate import tabulate
data = [["NAME", "PLACE", "AGE"], ["Amit", "leeds", "38"],
        ["Sheetal", "modinagar", "38"], ["Avyaan", "2", "ggn"],
        ["Ashita", "US", "10"]]
print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
