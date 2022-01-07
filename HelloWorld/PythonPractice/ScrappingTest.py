import requests
from bs4 import BeautifulSoup

html = requests.get("https://en.wikipedia.org/wiki/Comparison_of_programming_languages")
soup  = BeautifulSoup(html.content,'html.parser')

#print(soup.prettify())
tables = soup.findAll('table',{"class":"wikitable"}).th.a['href']
print(tables)