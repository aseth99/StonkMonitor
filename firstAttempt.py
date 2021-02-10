import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://finance.yahoo.com/quote/FLT.V?p=FLT.V&.tsrc=fin-srch'
# url = 'https://finance.yahoo.com/quote/BB.TO?p=BB.TO&.tsrc=fin-srch'

ticker = input("what stonk you want the price of? ")

url = "https://finance.yahoo.com/quote/"+ticker+"?p="+ticker+"&.tsrc=fin-srch"

try:
	page = urlopen(url)
except:
	print('Error opening the URL')

soup = bs4.BeautifulSoup(page,'html.parser')

soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})

soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text

def parsePrice():
    url = 'https://finance.yahoo.com/quote/FLT.V?p=FLT.V&.tsrc=fin-srch' 
    page = urlopen(url)
    price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return price

print("The current price for "+ ticker+" is: "+str(parsePrice()))