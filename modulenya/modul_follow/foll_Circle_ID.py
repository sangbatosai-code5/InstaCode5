import keyboard

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
#keyboard = KeyboardController()
#mouse = MouseController()

from time import sleep

from tqdm import tqdm
from tqdm.auto import tqdm
from tqdm import tqdm , trange

import random

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options

import pyfiglet

import os

#FILES IMPORT BELLOW
#import banner
import modulenya.modul_login.creditsPy
##########################################

White=("\033[0m")
Green=("\033[1;33m")
Blue=("\033[1;34m")
Grey=("\033[1;30m")
Reset=("\033[0m")
Red=("\033[1;31m")




##########################################
class FID:
	def __init__(self):
		
		
		print ()
		print ("===============================================================")
		print("F O L L O W by")
		result = pyfiglet.figlet_format("Circle - ID")
		print(result)
		print ("                                          -SANGBATOSAI | CODE5-")
		print ("         The Quieter You Become, The More You Are Able To Hear.")
		print ("                                                              -")
		print ("                                                    NGOPI ITEM.")
		print ("---------------------------------------------------------------")
		print ()
		
		
		self.idnya =           str(input(Reset+' [-] ID/Username    		: '+Green+''))
		#self.jmlfollower =           float(input(Reset+' [-] Target A     		: '+Green+''))		
		self.targetakun =           float(input(Reset+' [-] Target B    		: '+Green+''))
		
		self.iUser = modulenya.modul_login.creditsPy.username
		self.iPass = modulenya.modul_login.creditsPy.password

		print (Reset+"")
		print ()
		print ("===============================================================")
		print ()
		print ('Proses Dimulai ...')
		print ()
		
	def loginakun(self):
		self.driver_path = "/home/sangbatosai/HXBOTS/WebDriver/geckodriver"
		self.mybrowser = webdriver.Firefox(executable_path=self.driver_path)
		mybrowser=self.mybrowser
		mybrowser.implicitly_wait(20)
		mybrowser.get("https://www.instagram.com/")
		mybrowser.maximize_window()
		
		iUser = self.iUser
		iPass = self.iPass
		targetakun = self.targetakun
		#jmlfollower =self.jmlfollower
		
		sleep(2)
		element1000 = mybrowser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
		#element1000.click()
		# OR
		element1000.send_keys(iUser)
		print("Memasukan Username")
		sleep(2)
		
		# 
		sleep(2)
		element1002 = mybrowser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
		#element1002.click()
		# OR
		element1002.send_keys(iPass)
		print("Memasukan Password")
		sleep(2)
		
		# Button Login
		sleep(2)
		element1003 = mybrowser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
		element1003.click()
		sleep(2)
		
		# Button NOT NOW
		sleep(2)
		element1004 = mybrowser.find_element_by_xpath("//button[contains(.,'Not Now')]")
		element1004.click()
		print("Proses Login Selesai")
		sleep(2)
		
	def mencari(self):
		mybrowser=self.mybrowser
		idnya=self.idnya
		print("Proses Mencari Profile username @"+idnya+"")
		# Searching hashtag
		element1 = mybrowser.get("https://www.instagram.com/"+idnya+"/")
		sleep(2)


	def cek_followernya(self):
		mybrowser=self.mybrowser
		targetakun = self.targetakun
		print("Proses Membuka Followers")
		mybrowser.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
		sleep(2)
		
		locFoll = mybrowser.find_elements_by_xpath("//main[contains(@class,'o64aR')]//li[3]//a[1]")
		locFollA = mybrowser.find_elements_by_xpath("//main[contains(@class,'o64aR')]")
		popupA = mybrowser.find_element_by_xpath("//div[contains(@class,'isgrP')]")
		
		jmlFoll=len(mybrowser.find_element_by_xpath("//li[2]/a/span").text)
		scrollnya = mybrowser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', locFoll)
		jmlUFoll = targetakun
		
		n=0
		while n < jmlUFoll:
			for follower in locFollA:
				follow = mybrowser.find_elements_by_xpath("//button[contains(text(), 'Follow')]")
				i = 1
				for i in range(int(jmlFoll/2)):
					for follower in follow:
						if(i != 1):
							sleep(2)
							mybrowser.find_element_by_xpath("(//button[@class='sqdOP  L3NKy   y3zKF     '][contains(.,'Follow')])[1]").click()
							
						if(len(mybrowser.find_elements_by_xpath("//button[contains(text(), 'Following')]")) > 0):
							continue
						if(len(mybrowser.find_elements_by_xpath("//button[contains(text(), 'Unfollow')]")) > 0):
							mybrowser.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
						if(i > 6):
							continue
						sleep(1)
						sleep(random.randint(500,1000)/1000)
						print(Blue+"Extract friends %",round((i/(jmlFoll/2)*100),2),"from","%100"+Reset+"")
						i+=1
					sleep(3)
					mybrowser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popupA)
					sleep(2)
				print(Blue+"Follow ke-", i,""+Reset)
			n+=1
		mybrowser.close()	

# //button[contains(.,'Follow')]
