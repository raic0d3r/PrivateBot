# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 03:07:20 2020

@author: Rai
"""

import cfscrape, getpass, os
from platform import system
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
def siteisup(url):
    try:
        scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
        # Or: scraper = cfscrape.CloudflareScraper()  # CloudflareScraper inherits from requests.Session
        response = scraper.get("https://api.downfor.cloud/httpcheck/"+url, timeout=20).content  # => "<!DOCTYPE html><html><head>..."
#        print response
        if '"statusText":"OK"' in response:
            print '[{}Site is UP]: {} {}	       ====> {}    '.format(sb, sd, url, fg)
            open('siteisup.txt', 'a').write(url+'\n')
        else:
            print '[{}Site is Down]: {} {}	       ====> {}    '.format(sb, sd, url, fr)
    except:
        pass 

banners()
def passfor():		
    list = open(raw_input("List : "),'r').readlines()
    for url in list:
    	try:
           url = url.rstrip()    	
           data=siteisup(url)
        except:
            pass    

Passwd = getpass.getpass("Give Passwd : ")
if "" in Passwd:
	passfor()
else:
	exit()    