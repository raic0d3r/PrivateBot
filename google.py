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
 
 
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
 
def google(): 
    page = 1
    while True:
        url = 'https://www.google.com/search?q='
        page = page + 1
#        sess = requests.session()

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
            'Content-Type': 'text/html',
        }

        Open = requests.get(url+"inurl:/wp-content/plugins/revslider/"+"&num=100&hl=EN&start=" + str(page), headers=headers, timeout=10)
        soup = BeautifulSoup(Open.content, "html5lib")
        links = soup.findAll("a")
        for link in links :
            link_href = link.get('href')
            if "url?q=" in link_href and not "webcache" in link_href:
                print link.get('href').split("?q=")[1].split("&sa=U")[0]
                      #print result                      
                save = open("googleresults.txt","a")
                save.write(link.get('href').split("?q=")[1].split("&sa=U")[0] + '\n')
                save.close()

        if page > 50:
           sys.exit()
        else:
           continue
    
def passfor():		
    list = raw_input("List : "),'r'.readlines()
    for url in list:
    	try:
           url = url.rstrip()    	
           data=hackertarget(url)
        except:
            pass                   

Passwd = getpass.getpass("Give Passwd : ")
if "" in Passwd:
	google()
else:
	exit()    