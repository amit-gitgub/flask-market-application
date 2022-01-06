import requests
from bs4 import BeautifulSoup
import csv

"""
This Program is to scrap the web front end means HTML source. In webscrapping normally 3 modules are used. requests,  BeautifulSoup and csv. 
For clear understanding the code please refer to the article https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

"""

def scrapWeb(url):
    html = requests.get(url)
    #print(html.content)
    soup = BeautifulSoup(html.content, 'html.parser')
    table = soup.find('div', attrs={'id':'all_quotes'})
    #print(table.prettify())
    quoteList = []
    for row in soup.findAll('div', attrs={'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
        quoteDict = {}
        quoteDict['URL'] = row.a['href']
        quoteDict['Image'] = row.img['src']
        quoteDict['Line'] = row.img['alt'].split("#")[0]
        #print(quoteDict)
        quoteList.append(quoteDict)
    print(quoteList)
    filename = 'quotes.csv'
    with open(filename, 'w', newline='') as file:
        w = csv.DictWriter(file, ['URL','Image','Line'])
        w.writeheader()
        for quote in quoteList:
            w.writerow(quote)

scrapWeb("https://www.passiton.com/inspirational-quotes")