import sys, re, getpass, requests
import cfscrape, socket, os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import time as timer	
from multiprocessing.dummy import Pool
from colorama import Fore								
from colorama import Style
####### Colors	 ######	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										
#######################
proxies = {
    'http': 'socks5://localhost:9050',
    'https': 'socks5://localhost:9050'
}
def banners():
    try:
        os.mkdir('logs')
    except:
        pass
        
    banner = """{}

     _______            __                        __                _______               __     
    /       \          /  |                      /  |              /       \             /  |    
    $$$$$$$  | ______  $$/  __     __  ______   _$$ |_     ______  $$$$$$$  |  ______   _$$ |_   
    $$ |__$$ |/      \ /  |/  \   /  |/      \ / $$   |   /      \ $$ |__$$ | /      \ / $$   | {} 
    $$    $$//$$$$$$  |$$ |$$  \ /$$/ $$$$$$  |$$$$$$/   /$$$$$$  |$$    $$< /$$$$$$  |$$$$$$/   
    $$$$$$$/ $$ |  $$/ $$ | $$  /$$/  /    $$ |  $$ | __ $$    $$ |$$$$$$$  |$$ |  $$ |  $$ | __ 
    $$ |     $$ |      $$ |  $$ $$/  /$$$$$$$ |  $$ |/  |$$$$$$$$/ $$ |__$$ |$$ \__$$ |  $$ |/  |{}
    $$ |     $$ |      $$ |   $$$/   $$    $$ |  $$  $$/ $$       |$$    $$/ $$    $$/   $$  $$/ 
    $$/      $$/       $$/     $/     $$$$$$$/    $$$$/   $$$$$$$/ $$$$$$$/   $$$$$$/     $$$$/  
    {}                                                                                         
                                                                      ->>  PrivateBot  <<-     
                                                                      ->>  Coded by RaiC0d3r  <<-                                                                                              

		\n""".format(fg, fr, fg, sn)
		
    print(banner)
        
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
        
def getoption():
    print("{}[1]{} Get Ip from Site".format(fg, fw))
    print("{}[2]{} IP Range".format(fg, fw))
    print("{}[3]{} Live IP/Site Checker".format(fg, fw))
    print("{}[4]{} Reverse IP".format(fg, fw))
    choiceoption=input('Put Number => ')
    if choiceoption=='1':
        start_raw = input("\n\033[92m[!]\033[91m ENTER LIST OF WEBSITES : ")
        try:
            with open(start_raw, 'r') as f:
                url = f.read().splitlines()
        except IOError:
            pass
        url = list((url))  
        start = timer()
        ThreadPool = Pool(100)
        Threads = ThreadPool.map(getipfromsite, url)
        print('PrivateBot Finished in : ' + str(timer() - start) + ' seconds')
        
    elif choiceoption=='2':
        start_raw = input("\n\033[92m[!]\033[91m ENTER LIST OF WEBSITES : ")
        try:
            with open(start_raw, 'r') as f:
                url = f.read().splitlines()
        except IOError:
            pass
        start = timer()
        ThreadPool = Pool(100)
        Threads = ThreadPool.map(iprangee, url)
        print('PrivateBot Finished in : ' + str(timer() - start) + ' seconds')
        
    elif choiceoption=='3':
        start_raw = input("\n\033[92m[!]\033[91m ENTER LIST OF WEBSITES : ")
        try:
            with open(start_raw, 'r') as f:
                url = f.read().splitlines()
        except IOError:
            pass
        start = timer()
        ThreadPool = Pool(100)
        Threads = ThreadPool.map(isitdown, url)
        print('PrivateBot Finished in : ' + str(timer() - start) + ' seconds')
        
    elif choiceoption=='4':
        print("{}[1]{} Hackertarget" .format(fg, fw))
        print("{}[2]{} ViewDNS" .format(fg, fw))
        print("{}[3]{} Bing Reverse" .format(fg, fw))
        choicrev=input('Put Number => ')
        if choicrev=='1':
            start_raw = input("\n\033[92m[!]\033[91m ENTER LIST OF WEBSITES : ")
            try:
                with open(start_raw, 'r') as f:
                    url = f.read().splitlines()
            except IOError:
                pass
            start = timer()
            ThreadPool = Pool(100)
            Threads = ThreadPool.map(hackertarget, url)
            print('PrivateBot Finished in : ' + str(timer() - start) + ' seconds')
            
        if choicrev=='2':
            start_raw = input("\n\033[92m[!]\033[91m ENTER LIST OF WEBSITES : ")
            try:
                with open(start_raw, 'r') as f:
                    url = f.read().splitlines()
            except IOError:
                pass
            start = timer()
            ThreadPool = Pool(100)
            Threads = ThreadPool.map(viewdns, url)
            print('PrivateBot Finished in : ' + str(timer() - start) + ' seconds')
            
        if choicrev=='3':
            start_raw = input("\n\033[92m[!]\033[91m ENTER LIST OF WEBSITES : ")
            try:
                with open(start_raw, 'r') as f:
                    url = f.read().splitlines()
            except IOError:
                pass
            start = timer()
            ThreadPool = Pool(100)
            Threads = ThreadPool.map(bingreverse, url)
            print('PrivateBot Finished in : ' + str(timer() - start) + ' seconds')

def getipfromsite(url):
    try:
        url = url
        try:
            ip = socket.gethostbyname(url)
            print('[{}URL to IP]: {} {}	       ====> {}{}    '.format(sb, sd, url, fg, ip))
            open('logs/webtoip.txt', 'a').write(ip+'\n')
        except:
            pass
        lines_seen = set() # holds lines already seen
        outfile = open("webtoip.txt", "w")
        for line in open('logs/webtoip.txt', "r"):
            if line not in lines_seen: # not a duplicate
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()         
    except:
        pass

def iprangee(url):
    try:
        ip = socket.gethostbyname(url)
        parts = ip.split('.')
        part_0 = parts[0]
        part_1 = parts[1]
        part_2 = parts[2]
        part_3 = parts[3]
        sep = '.'
        for x in range(1, 256):
            result = (part_0 + sep + part_1 + sep + part_2 + sep + str(x))
            print(result)     
            open('logs/iprangee.txt', 'a').write(result+'\n')
        lines_seen = set() # holds lines already seen
        outfile = open("iprange.txt", "w")
        for line in open('logs/iprangee.txt', "r"):
            if line not in lines_seen: # not a duplicate
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()         
    except:
        pass

def isitdown(url):
    try:
        request = requests.get(url, timeout=10)
        kode = request.status_code        
        if kode != 500  or kode != 501  or kode != 502  or kode != 503  or kode != 301  or kode != 302  or kode != 303  or kode != 304	or kode != 443 :
            print('[{}Site]: {} {}	  ==> {}{} isitdown     {}{} Up  '.format(sb, sd, url, fc,fc, sb,fg))
            open('siteisup.txt', 'a').write(url+'\n')
    except:
        print('[{}Site]: {} {}	  ==> {}{} isitdown     {}{} Down  '.format(sb, sd, url, fc,fc, sb,fr))
        
#################reverse###################
def hackertarget(url): 
    for x in range(1):
        renew_tor_ip()
        ipAddresss = requests.get("http://api.ipify.org", proxies=proxies).text 
        print('Current IP: '+ ipAddresss)
        ipAddress = requests.get('http://api.hackertarget.com/reverseiplookup/?q='+url, proxies=proxies).text
        print('Current Url: '+ url)
        if '.com' in ipAddress:          
            print(ipAddress)
            save = open("logs/hackertarget.txt","a")
            save.write(ipAddress.text + '\n')
            save.close()
            hackertargetdprm()           
            time.sleep(1)
        else:
            return

def viewdns(url):
    scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
    # Or: scraper = cfscrape.CloudflareScraper()  # CloudflareScraper inherits from requests.Session
    r = scraper.get("https://viewdns.info/reverseip/?host="+ url +"&t=1")
    r1 = re.findall ("<td>((?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})</td>",r.content)
    for site in r1:
        if site.startswith('http://'):
            site = site.replace('http://', '')
        elif site.startswith('https://'):
            site = site.replace('https://', '')
        else:
            pass
        print('[{}Found]: {} {}	       ====> {}{}    '.format(sb, sd, site, fg, url))
        with open("ipx.txt", 'a') as f:
            if 'go.microsoft.com' in site:
                pass
            else:
                f.write('http://' + str(site + '\n'))

def bingreverse(url):
    try:
        while True:
#            ips = url
            try:
                ip = socket.gethostbyname(url)
            except:
                sys.exit()
            next = 0
            while next <= 500:
                url = "http://www.bing.com/search?q=ip%3A" + ip + "&first=" + str(next) + "&FORM=PORE"
                sess = requests.session()
                cnn = sess.get(url, timeout=5)
                next = next + 10
                finder = re.findall(
                    '<h2><a href="((?:https://|http://)[a-zA-Z0-9-_]+\.*[a-zA-Z0-9][a-zA-Z0-9-_]+\.[a-zA-Z]{2,11})',
                    cnn.text)
                for url in finder:
                    if url.startswith('http://'):
                        url = url.replace('http://', '')
                    elif url.startswith('https://'):
                        url = url.replace('https://', '')
                    else:
                        pass
                    print('[{}Found]: {} {}	       ====> {}{}    '.format(sb, sd, url, fg, ip))
                    with open("logs/ipx.txt", 'a') as f:
                        if 'go.microsoft.com' in url:
                            pass
                        else:
                            f.write('http://' + str(url + '\n'))
            lines = open("logs/ipx.txt", 'r').read().splitlines()
            lines_set = set(lines)
            count = 0
            					
            for line in lines_set:
                with open("logs/ipx.txt", 'a') and open("Result/binglist.txt", 'a') as xx:
                    count = count + 1
                    xx.write(line + '\n')
            print("Total Sites Found: " + str(count))
#            q.task_done()
    except IndexError:
        sys.exit()

##################end reverse############
banners()
licensed = requests.get("https://raw.githubusercontent.com/raic0d3r/PrivateBot/main/licensed").text
get_key = input("Enter Your License : ")
if get_key in licensed:
	getoption()
else:
	exit()