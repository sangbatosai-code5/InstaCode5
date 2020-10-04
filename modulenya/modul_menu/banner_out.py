import pyfiglet
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options


##########################################

White="\033[0m"
Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"

##########################################



def selesai():
	print ()
	print ()
	print ("===============================================================")
	print ("                        "+Blue+"S E L E S A I")
	print ("                       "+Blue+"C R E D I T  B Y")
	print ("                "+Blue+"S A N G  B A T O S A I | Code5")
	print ()
	print (""+Green+"===============================================================")
	print ("===============================================================")
	print ()
	print ()
	print (Reset)
	sleep(2)
	sys.exit

