#!/usr/bin/python27
import os, re, sys, socket, urllib2, binascii, time, json, random, threading, requests
from bs4 import BeautifulSoup
res = requests.get('https://www.techadvisor.co.uk/review/smartphones/oppo-a9-2020-3779726/', headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(res.text,"lxml")
for text in soup.select("body div"):
    file = ':'.join([item.text for item in text.select("p")])
    file = file.replace('METRO(.*)','test')   
    #open('files.txt', 'a').write(file+'\n')    
    print file
