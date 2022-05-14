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
		
def iprangee(url):
    try:
        ip = socket.gethostbyname(url)
        parts = url.split('.')
        part_0 = parts[0]
        part_1 = parts[1]
        part_2 = parts[2]
        part_3 = parts[3]
        sep = '.'
        for x in range(1, 256):
            result = (part_0 + sep + part_1 + sep + part_2 + sep + str(x))
            print result       
            open('iprangee.txt', 'a').write(result+'\n')
    except:
        pass

banners()

def passfor():		
    list = open(raw_input("List : "),'r').readlines()
    for url in list:
    	try:
           url = url.rstrip()    	
           data=iprangee(url)
        except:
            pass    

Passwd = getpass.getpass("Give Passwd : ")
if "" in Passwd:
	passfor()
else:
	exit()