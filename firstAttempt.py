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

# soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})

# soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text

def parsePrice():
    url = "https://finance.yahoo.com/quote/"+ticker+"?p="+ticker+"&.tsrc=fin-srch"
    page = urlopen(url)
    # <div class="D(ib) Mend(20px)" data-reactid="31"><span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid="32">17.02</span><span class="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)" data-reactid="33">-0.45 (-2.58%)</span><div id="quote-market-notice" class="C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm" data-reactid="34"><span data-reactid="35">At close:  4:00PM EST</span></div></div>
    price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find_all('span')
    # change = soup.find('span',{'data-reactid': '33'}).text
    counter = 0
    for x in price:

	    print(information(counter) + x.text)
	    counter = counter + 1

    return price

def zero():
    return "Current Price: "
 
def one():
    return "$$ Change (% Change) : "
 
def two():
    return "Time "
 
switcher = {
        0: zero,
        1: one,
        2: two
    }
 
 
def information(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()



parsePrice()