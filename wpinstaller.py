import re, requests, os, sys
import html, urllib.request, urllib.error
from time import time as timer  
from multiprocessing.dummy import Pool
from pathlib import Path
from colorama import Fore                               
from colorama import Style
#from web import web
####### Colors   ###### 
fr  =   Fore.RED                                            
fc  =   Fore.CYAN                                           
fw  =   Fore.WHITE                                          
fg  =   Fore.GREEN                                          
sd  =   Style.DIM                                           
sn  =   Style.NORMAL                                        
sb  =   Style.BRIGHT
                                        
#######################

def banners():
    try:
        os.mkdir('logs')
    except:
        pass
        
    banner = """{}

                   ...          
                 ;::::;           ::
               ;::::; :;        :::::: 
              ;::::;  :;     WP-Installer
             ;:::::'   :;     By RaiC0d3r
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\{}
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO  {}
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#                                                                                            

        \n""".format(fg, fr, fg, sn)
        
    print(banner)


Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

def wpinstall(url):
    try:
        if url.startswith('http://'):
            url = url.replace('http://', '')
        elif url.startswith('https://'):
            url = url.replace('https://', '')
        else:
            pass

        list_path = ['/','/new', '/wp', '/wordpress']
        for path in list_path:
            #check = requests.get("https://" + url + path + "/wp-admin/setup-config.php" ,headers=headers)
            check = urllib.request.urlopen("https://" + url + path + "/wp-admin/setup-config.php").read()
            mystr = check.decode("utf8")
            if '<a href="setup-config.php?step=1' in mystr:
                print('[{}WordPress]: {} {}   ==> {}{} Wp Install     {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg))
                open('WP-install.txt', 'a').write(url + path + "/wp-admin/setup-config.php" + "\n")
            else:
                print('[{}WordPress]: {} {}   ==> {}{} Wp Install     {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr))

    except urllib.error.URLError:
        pass

    except urllib.error.HTTPError:
        pass        

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except:
        pass

banners()
start_raw = input("\n\033[92m[!]\033[91m WEBSITES LIST WITHOUT http:// or https:// : ")
try:
    with open(start_raw, 'r') as f:
        url = f.read().splitlines()
except IOError:
    pass
url = list((url))
start = timer()
ThreadPool = Pool(100)
Threads = ThreadPool.map(wpinstall, url)
print('PrivateBot Finished in : ' + str(timer() - start) + ' seconds')
