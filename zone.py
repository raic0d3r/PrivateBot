#!/usr/bin/python

# Coded By RaiC0d3r 
# Muslim Hackers

import requests, re,urllib, urllib2, os, sys, codecs,binascii, json, argparse, getpass			
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
from random import sample as rand
from Queue import Queue				   		
from platform import system
from urlparse import urlparse
from optparse import OptionParser	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init												
init(autoreset=True)
										
															
####### Colors	 ######	
	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										

####################### 

def banners():

	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
		
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
                                                                      ->>  Coded by RaiC0d3r  <<-                                                                                              

		\n""".format(fg, fr, fg, sn)
		
		print banner
		
def passfor():		
    __Defacer = raw_input("Name_of_defacer : ")
    __ZH = raw_input("ZHE : ") 
    __ZHE = raw_input("ZHE : ")		
    __PHPSESSID = raw_input("PHPSESSID : ") 	
    page = 1
    print ('Notifier is : ' + __Defacer)
    while True:
        url = 'http://zone-h.com/archive/notifier='
        page = page + 1
        sess = requests.session()

        my_cookie = {
            'ZHE': __ZHE,
            'ZH': __ZH,
            'PHPSESSID': __PHPSESSID
        }

        Open = sess.get(url+__Defacer + '/page=' + str(page), cookies=my_cookie, timeout=10)
        print Open.text
        Hunt_urls = re.findall('<td>(.*)\n							</td>', Open.content)
        for xx in Hunt_urls:
            print xx.split('/')[0]
            with open('zone.txt', 'a') as rr:
                rr.write(xx.split('/')[0] + '\n')

        if page > 50:
           sys.exit()
        else:
           continue

banners()

Passwd = getpass.getpass("Give Passwd : ")
if "" in Passwd:
	passfor()
else:
	exit()