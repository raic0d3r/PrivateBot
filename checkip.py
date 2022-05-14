import requests
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

renew_tor_ip()
ipAddresss = requests.get("http://api.ipify.org", proxies=proxies).text         
print ipAddresss