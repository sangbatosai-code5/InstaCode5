import requests, sys, threading, time, os, random
from random import randint
CheckVersion = str(sys.version)
import keyboard
from time import sleep
import pyfiglet


#MODULE IMPORT
#from InstaCode5 import pilihanmenu

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
class HeaderHelp:
	def __init__(self):
		self.print_logo()
		self.rulesnya()
		self.menupilih_backtoMenu()
	
	def print_logo(self): 
		clear = "\x1b[0m"
		colors = [36, 32, 34, 35, 31, 37]
		x = """
[Lets Build Your Own Code]
| | | | | ____| | |     |  _ \ 
| |_| | |  _|   | |     | |_) |
|  _  | | |___  | |___  |  __/ 
|_| |_| |_____| |_____| |_|    

GitHub.com/sangbatosai-code5                    
Development V.1.Aug2020       
    """
		for N, line in enumerate(x.split("\n")):
			sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
			time.sleep(0.05)

	def rulesnya(self):
		file_rules = open("modulenya/modul_menu/instagram-rules", "r")
		baca_rules = file_rules.read()
		file_rules.close()
		print(baca_rules)
		
		

	def menupilih_backtoMenu(self):
		sleep(1)
		print()
		print(Green+'PILIHAN KEMBALI KE MENU')
		while True:
			query = input('Apakah ingin Kembali ke menu? [Y/y or N/n] ')
			Fl = query[0].lower()
			if query == '' or not Fl in ['y','n']:
				print()
			else:
				break 
	            
		if Fl == 'y':
			print("Yes")
			pass
		if Fl == 'n':
			exit()
			

