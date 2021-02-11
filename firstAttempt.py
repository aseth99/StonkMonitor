import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

ticker = input("what stonk you want the price of? ")

url = "https://finance.yahoo.com/quote/"+ticker+"?p="+ticker+"&.tsrc=fin-srch"

try:
	page = urlopen(url)
except:
	print('Error opening the URL')

soup = bs4.BeautifulSoup(page,'html.parser')

def parsePrice():
	url = "https://finance.yahoo.com/quote/"+ticker+"?p="+ticker+"&.tsrc=fin-srch"
	page = urlopen(url)
	price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find_all('span')
	return price

stonkInfo = parsePrice()

print("Current Price: " + stonkInfo[0].text)
print("$$ Change (% Change) : " + stonkInfo[1].text)
print("Time: " + stonkInfo[2].text)