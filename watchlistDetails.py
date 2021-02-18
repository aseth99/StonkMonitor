import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from datetime import date
import os


def writeToCSV(name,info,summary):
	today = date.today()
	fileName = name + '.csv'
	try:
		os.mkdir("./"+str(today))
	except OSError as e:
		print("Directory Exists")

	with open("./"+str(today)+'/'+ fileName, 'a') as stonk_file:

		fieldnames = ['Name', 'Value']
		stonk_writer = csv.DictWriter(stonk_file, fieldnames=fieldnames)

		stonk_writer.writeheader()
		stonk_writer.writerow({'Name': 'Info for Stonk:', 'Value': name})
		stonk_writer.writerow({'Name': 'Current Price:', 'Value': info[0].text})
		stonk_writer.writerow({'Name': '$$ Change (% Change) :', 'Value': info[1].text})
		stonk_writer.writerow({'Name': 'Time:', 'Value': info[2].text})
		
		for x in range(0, len(summary), 2):
			stonk_writer.writerow({'Name': summary[x].text, 'Value': summary[x+1].text})
		else:
			stonk_writer.writerow({'Name': '-------', 'Value': '-----'})

		print("Today's date:", today)
		return

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
		# print("Current Price: " + stonkInfo[0].text)
		# print("$$ Change (% Change) : " + stonkInfo[1].text)
		# print("Time: " + stonkInfo[2].text + "\n")
		summaryInfo = soup.find('div',{'id': 'quote-summary'}).find_all('td')

		writeToCSV(stonkName,stonkInfo,summaryInfo)
		
		# for x in range(0, len(summaryInfo), 2):
		# 	# print(summaryInfo[x].text + ": " +summaryInfo[x+1].text)
		# else:
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

if __name__ == "__main__":
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