import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

def stonkInfoFunc(ticker):
	url = "https://finance.yahoo.com/quote/"+ticker+"?p="+ticker+"&.tsrc=fin-srch"

	try:
		page = urlopen(url)
	except:
		print('Error opening the URL')
		return

	soup = bs4.BeautifulSoup(page,'html.parser')

	stonkInfo = parsePrice(ticker)
	if stonkInfo == 0:
		return None
	else:
		stonkName = soup.find('div',{'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'}).find('h1').text
		print("\nInfo for Stonk: "+ stonkName+"\n")
		print("Current Price: " + stonkInfo[0].text)
		print("$$ Change (% Change) : " + stonkInfo[1].text)
		print("Time: " + stonkInfo[2].text + "\n")
		summaryInfo = soup.find('div',{'id': 'quote-summary'}).find_all('td')

		for x in range(0, len(summaryInfo), 2):
			print(summaryInfo[x].text + ": " +summaryInfo[x+1].text)
		else:
			print("-------------------")
	return None

def parsePrice(ticker):
	url = "https://finance.yahoo.com/quote/"+ticker+"?p="+ticker+"&.tsrc=fin-srch"
	page = urlopen(url)
	soup = bs4.BeautifulSoup(page,'html.parser')
	try:
		price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find_all('span')
	except:
		print('Error getting info on stock: '+ticker)
		return 0
	price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find_all('span')
	return price

# stonkInfoFunc("ATZ.TO")
# stonkInfoFunc("BNS.TO")
# stonkInfoFunc("GOOS.TO")
# stonkInfoFunc("FLT.V")
# stonkInfoFunc("ENB.TO")
# stonkInfoFunc("ERE-UN.TO")
# stonkInfoFunc("FFH.TO")
# stonkInfoFunc("INO-UN.TO")
# stonkInfoFunc("NWH-UN.TO")
# stonkInfoFunc("OPEN")
# stonkInfoFunc("RY.TO")
# stonkInfoFunc("SGR-UN.TO")
# stonkInfoFunc("SRU-UN.TO")
# stonkInfoFunc("XBC.TO")
# stonkInfoFunc("ACIC")
# stonkInfoFunc("N.V")
# stonkInfoFunc("VCN.TO")
# stonkInfoFunc("VEE.TO")
# stonkInfoFunc("VRE.TO")
# stonkInfoFunc("XEF.TO")
# stonkInfoFunc("XSP.TO")
# stonkInfoFunc("XUU.TO")
# stonkInfoFunc("0P000073OF.TO")


watchlist = [
			"ATZ.TO",
			"BNS.TO",
			"GOOS.TO",
			"FLT.V",
			"ENB.TO",
			"ERE-UN.TO",
			"FFH.TO",
			"INO-UN.TO",
			"NWH-UN.TO",
			"OPEN",
			"RY.TO",
			"SGR-UN.TO",
			"SRU-UN.TO",
			"XBC.TO",
			"ACIC",
			"N.V",
			"VCN.TO",
			"VEE.TO",
			"VRE.TO",
			"XEF.TO",
			"XSP.TO",
			"XUU.TO",
			"0P000073OF.TO"
			]
for x in watchlist:
	stonkInfoFunc(x)