import requests
from bs4 import BeautifulSoup
import csv

"""
This Program is to scrap the web front end means HTML source. In webscrapping normally 3 modules are used. requests,  BeautifulSoup and csv. 
For clear understanding the code please refer to the article https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

"""


html = requests.get("http://123hindijokes.com/santa-banta-jokes/")
#print(html.content)
soup = BeautifulSoup(html.content, 'html.parser')
table = soup.findAll('ul', attrs={'class':'statusList'})
row = soup.findAll('li')
jokes = []
#print(table)
for i in table:
    for j in i.findAll('li'):
        jokes.append(j.getText())

with open('jokes.txt', 'w', encoding="utf-8") as f:
    for item in jokes:
        f.writelines(item)
        f.write('\n\n')



