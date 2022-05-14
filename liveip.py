#!/usr/bin/python

# Coded By RaiC0d3r 
# Muslim Hackers

import requests, re, os, sys, getpass, socket			
from time import time as timer	
import time
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
		
def liveip(url):
    try:
        response = requests.get('http://'+url)
        if not response.status_code == 200:       
           print '[{}Died IP]: {} {}	       ====> {}{}    '.format(sb, sd, url, fr, ip)
        else:
            print '[{}Live IP]: {} {}	       ====> {}{}    '.format(sb, sd, url, fg, ip)    
            open('liveip.txt', 'a').write(url+'\n')            
    except:
        pass 

banners()

def passfor():		
    list = open(raw_input("List : "),'r').readlines()
    for url in list:
    	try:
           url = url.rstrip()    	
           data=liveip(url)
        except:
            pass    

Passwd = getpass.getpass("Give Passwd : ")
if "" in Passwd:
	passfor()
else:
	exit()