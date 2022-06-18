import urllib.request
import socket
import socks
from stem import Signal
from stem.control import Controller
from time import time as timer
from multiprocessing.dummy import Pool

def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def hackertarget(url):
    try:
        for x in range(1):
            renew_tor_ip()
            socks.set_default_proxy(socks.SOCKS5, "localhost",port=9050)
            socket.socket = socks.socksocket
            res1=urllib.request.urlopen('http://api.ipify.org', timeout=10).read().decode("utf-8")
            res=urllib.request.urlopen('http://api.hackertarget.com/reverseiplookup/?q='+url, timeout=20).read().decode("utf-8")
            if '.com' in res:
                print("Scanning ==>"+url)          
                print (res)            
                save = open("hackertarget.txt","a")
                save.write(res + '\n')
                save.close()
                #hackertargetdprm()           
                time.sleep(1)
            else:
                return

    except urllib.error.URLError:
        pass

    except urllib.error.HTTPError:
        pass        

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except:
        pass

def passfor():
    url = open(input("[!] ENTER LIST OF WEBSITES : "), 'r').read().splitlines()
    start = timer()
    ThreadPool = Pool(100)
    Threads = ThreadPool.map(hackertarget, url)

passfor()
