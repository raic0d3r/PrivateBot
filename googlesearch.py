import json
import time, getpass
import requests
from bs4 import BeautifulSoup
import re
import math
#from urllib.request import urlopen
from stem import Signal
from stem.control import Controller
 
proxies = {
    'http': 'socks5://localhost:9050',
    'https': 'socks5://localhost:9050'
}

url = "" 
 
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
 
def google(dork): 
    for x in range(1):
        renew_tor_ip()
        ipAddresss = requests.get("http://api.ipify.org", proxies=proxies).text 
        print ipAddresss
        results = 100
        #for i in range(pages) :
        #    start = i * 100
        next = 0
        while next <= 100:        
              page = requests.get("https://www.google.com/search?q="+dork+"&num=100&hl=EN&start=1" + str(next), proxies=proxies)
              soup = BeautifulSoup(page.content, "html5lib")
              links = soup.findAll("a")
              for link in links :
                  link_href = link.get('href')
                  if "url?q=" in link_href and not "webcache" in link_href:
                      print link.get('href').split("?q=")[1].split("&sa=U")[0]
                      #print result                      
                      save = open("googleresults.txt","a")
                      save.write(link.get('href').split("?q=")[1].split("&sa=U")[0] + '\n')
                      save.close()                      
                

Passwd = getpass.getpass("Give Passwd : ")
if "" in Passwd:
	dork = raw_input("what is you want search?  ")
	google(dork)

else:
	exit()    