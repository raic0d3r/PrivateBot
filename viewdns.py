import json
import time, getpass
import requests
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
 
def hackertarget(url): 
    #for x in range(1):
     #   renew_tor_ip()
      #  ipAddresss = requests.get("http://api.ipify.org", proxies=proxies).text 
       # print ipAddresss        
    ipAddress = requests.post('https://www.yougetsignal.com/tools/web-sites-on-web-server/', data = {'remoteAddress':url}, proxies=proxies).text
    print ipAddress
    time.sleep(1)
    
def passfor():		
    list = open(raw_input("List : "),'r').readlines()
    for url in list:
    	try:
           url = url.rstrip()    	
           data=hackertarget(url)
        except:
            pass                   

Passwd = getpass.getpass("Give Passwd : ")
if "" in Passwd:
	passfor()
else:
	exit()    