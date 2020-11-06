import keyboard

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

from time import sleep

from tqdm import tqdm
from tqdm.auto import tqdm
from tqdm import tqdm , trange


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
import modulenya.modul_login.creditsPy

##########################################

White=("\033[0m")
Green=("\033[1;33m")
Blue=("\033[1;34m")
Grey=("\033[1;30m")
Reset=("\033[0m")
Red=("\033[1;31m")




##########################################
class FLBACK:
	def __init__(self):
		
		
		print ()
		print ("===============================================================")
		print("F O L L O W  B A C K  followers")
		result = pyfiglet.figlet_format("FollBack")
		print(result)
		print ("                                          -SANGBATOSAI | CODE5-")
		print ("         The Quieter You Become, The More You Are Able To Hear.")
		print ("                                                              -")
		print ("                                                    NGOPI ITEM.")
		print ("---------------------------------------------------------------")
		print ()
		
		print (" NOTE !!! MAX FOLLOW 7-13 follows/hour or 100-150 follows/day")
		print(Reset+' [-] Tekan ENTER untuk memulai'+Green+'')

		
		self.iUser = modulenya.modul_login.creditsPy.username
		self.iPass = modulenya.modul_login.creditsPy.password
		self.urlProfile = modulenya.modul_login.creditsPy.url_profile
		
		iUser = self.iUser
		iPass = self.iPass
		iUrlProfile = self.urlProfile

		
		
		print (Reset+"")
		print ()
		print ("===============================================================")
		print ()
		print ('Proses Dimulai ...')
		print ()
	    

	def loginakun(self):
		self.driver_path = "/usr/bin/geckodriver"
		self.mybrowser = webdriver.Firefox(executable_path=self.driver_path)
		mybrowser=self.mybrowser
		mybrowser.get("https://www.instagram.com/")
		mybrowser.maximize_window()
		
		iUser = self.iUser
		iPass = self.iPass

		
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
		element1004 = mybrowser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
		element1004.click()
		print("Proses Login Selesai")
		sleep(2)
		
	def mencari(self):
		mybrowser=self.mybrowser
		iUser = self.iUser
		iUrlProfile = self.urlProfile

		print("Proses Membuka Profile Akun")
		# Searching Akun Profile
		element1 = mybrowser.get(iUrlProfile)
		sleep(3)
	
	def cek_follower(self):
		mybrowser=self.mybrowser
		sleep(2)
		locFoll = mybrowser.find_element_by_xpath("//main[contains(@class,'o64aR')]//li[2]//a[1]")
		self.mybrowser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', locFoll)
		popupA = mybrowser.find_element_by_xpath("//div[contains(@class,'isgrP')]")
		last_hgt, hgt=0,1
		while last_hgt != hgt:
			last_hgt = hgt
			sleep(1)
			hgt = self.mybrowser.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""", popupA)
				
		linkNama = popupA.find_elements_by_tag_name('a')
		nama = [name.text for name in linkNama if name.text != '']
		self.mybrowser.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button/div").click()
		return nama

			
	def daftar_belumFollBack(self):
		mybrowser=self.mybrowser
		print(Blue+"PROSES ANALISA FOLLOWING"+Reset)
		mybrowser.find_element_by_xpath("//a[contains(@href,'/following')]").click()
		following = self.cek_follower()
		
		print(Blue+"PROSES ANALISA FOLLOWERS"+Reset)
		mybrowser.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
		followers = self.cek_follower()
		
		self.dftrblmFollBack = [user for user in followers if user not in following]
		dftrblmFollBack = self.dftrblmFollBack
		totalBlmFollBack = len(dftrblmFollBack)
		print(dftrblmFollBack)
		print("TOTAL YANG BELUM DI FOLLBACK:",totalBlmFollBack)
		
		

	def menupilih_follback(self):
		mybrowser=self.mybrowser
		menupilihFollBack_y = self.menupilihFollBack_y
		sleep(1)
		print()
		print(Green+'PILIHAN FOLLOW BACK')
		print()
		while True:
			query = input('Apakah ingin FollBack?  ')
			Fl = query[0].lower()
			if query == '' or not Fl in ['y','n']:
				menupilihFollBack_y
				print()
			else:
				break 
	            
		if Fl == 'y':
			print("Yes")
			pass
		if Fl == 'n':
			exit()
			print("No")
			
	def menupilihFollBack_y(self):
		mybrowser=self.mybrowser
		dftrblmFollBack = self.dftrblmFollBack
		
		
		for blmFollBack in dftrblmFollBack:
			mybrowser.get("https://www.instagram.com/" + blmFollBack)
			sleep(2)
			
			if(len(mybrowser.find_elements_by_xpath("//button[contains(text(), 'Follow')]")) > 0):
				btn_follow = mybrowser.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()
			
			if(len(mybrowser.find_elements_by_xpath("//button[contains(text(), 'Follow')]")) < 0):
				continue
			
			if(len(mybrowser.find_elements_by_xpath("//*[contains(text(), 'This Account is Private')]")) > 0):
				# If they're private, we can't see their follower list, so skip them
				continue
			sleep(2)
			mybrowser.refresh()
			sleep(2)
		
		mybrowser.close()		
			
			

		
		

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
