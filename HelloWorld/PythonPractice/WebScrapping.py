import csv
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_programming_languages")
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())
table = soup.findAll("table", {"class":"wikitable"})[1]
rows = soup.findAll("tr")

with open("table.csv", "wt+", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for i in rows:
        row = []
        for cell in i.findAll(["td","th"]):
            row.append(cell.getText())
        writer.writerow(row)

a = pd.read_csv("table.csv")
print(a.head())

