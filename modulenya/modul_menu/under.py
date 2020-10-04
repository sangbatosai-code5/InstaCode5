import requests, sys, threading, time, os, random
from random import randint
CheckVersion = str(sys.version)
import keyboard
from time import sleep


import pyfiglet


#MODULE IMPORT

import modulenya.modul_menu.banner_out

import modulenya.modul_comment.comm_id
import modulenya.modul_comment.comm_htag
from modulenya.modul_comment.comm_htag import HTAG

#from modulenya.modul_follow.boost_id import *
import modulenya.modul_follow.foll_id
import modulenya.modul_follow.foll_htag
import modulenya.modul_follow.foll_back


##########################################
BgIjo=("\033[93m")
White=("\033[0m")
Green=("\033[1;33m")
Blue=("\033[1;34m")
Grey=("\033[1;30m")
Reset=("\033[0m")
Red=("\033[1;31m")

r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
rr = '\033[39m'
##########################################
print ("===============================================================")
class HeaderUnderConst:
	def __init__(self):
		self.print_logo()
	
	def print_logo(self): 
		clear = "\x1b[0m"
		colors = [36, 32, 34, 35, 31, 37]
		x = """
[Lets Build Your Own Code]
 _   _ _   _ ____  _____ ____    _   _  
| | | | \ | |  _ \| ____|  _ \  | | | |                              
| | | |  \| | | | |  _| | |_) | | | | |                              
| |_| | |\  | |_| | |___|  _ <  |_| |_|                              
 \___/|_| \_|____/|_____|_| \_\ (_) (_)      
  ____                _                   _   _                      
 / ___|___  _ __  ___| |_ _ __ _   _  ___| |_(_) ___  _ __  ___      
| |   / _ \| '_ \/ __| __| '__| | | |/ __| __| |/ _ \| '_ \/ __|     
| |__| (_) | | | \__ \ |_| |  | |_| | (__| |_| | (_) | | | \__ \     
 \____\___/|_| |_|___/\__|_|   \__,_|\___|\__|_|\___/|_| |_|___/     
GitHub.com/sangbatosai-code5                    
Development V.1.Aug2020       
    """
		for N, line in enumerate(x.split("\n")):
			sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
			time.sleep(0.05)

	
