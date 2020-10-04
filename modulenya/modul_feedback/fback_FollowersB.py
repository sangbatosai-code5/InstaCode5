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
class FeedBack:
	def __init__(self):
		
		
		print ()
		print ("===============================================================")
		print("FeedBack Service for followers - L I K E")
		result = pyfiglet.figlet_format("FEEDBACK FOLLOWERS")
		print(result)
		print ("                                          -SANGBATOSAI | CODE5-")
		print ("         The Quieter You Become, The More You Are Able To Hear.")
		print ("                                                              -")
		print ("                                                    NGOPI ITEM.")
		print ("---------------------------------------------------------------")
		print ()
		
		print (" NOTE !!! MAX FOLLOW 7-13 follows/hour or 100-150 follows/day")
		print (" NOTE !!! MAX LIKE 700 to 1000 a day")
		print (" NOTE !!! MAX COMMENT 150x")
		
		self.viewPost =           int(input(Reset+' [-] Jumlah Like Posting	: '+Green+''))
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
		self.driver_path = "/home/sangbatosai/HXBOTS/WebDriver/geckodriver"
		self.mybrowser = webdriver.Firefox(executable_path=self.driver_path)
		mybrowser=self.mybrowser
		mybrowser.implicitly_wait(10)
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
		self.nama = [name.text for name in linkNama if name.text != '']
		nama = self.nama
		self.mybrowser.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button/div").click()
		return nama
		
	def daftar_FollowersIng(self):
		mybrowser=self.mybrowser
		
		print(Blue+"PROSES ANALISA FOLLOWERS"+Reset)
		mybrowser.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
		followers = self.cek_follower()
		
		self.dftrFollWhitelists = [user for user in followers ]
		dftrFollWhitelists = self.dftrFollWhitelists

		print(Green)
		print("DAFTAR FOLLOWERS :")
		print(dftrFollWhitelists)
		print(Reset)
		print()
		print ("---------------------------------------------------------------")
		sleep(3)
	
	def prosesFeedback(self):
		sleep(2)
		mybrowser=self.mybrowser
		iUrlProfile = self.urlProfile
		iUser = self.iUser
		dftrFollWhitelists = self.dftrFollWhitelists
		print(Blue+"PROSES Mencari Posting"+Reset)
		
		for feedbackFoll in dftrFollWhitelists:
			mybrowser.get("https://www.instagram.com/" + feedbackFoll)
			sleep(2)
			
			print("Membuka Top Posting " + feedbackFoll)
			if(len(mybrowser.find_elements_by_class_name("eLAPa")) > 0):
				element2= mybrowser.find_element_by_class_name("eLAPa").click()
			if(len(mybrowser.find_elements_by_class_name("eLAPa")) < 0):
				print(Blue+"Akun Terdeteksi Belum ada Posting"+Reset)
				pass
			sleep(3)
			
			# Check LIKE
			sleep(2)
			if(len(mybrowser.find_elements_by_xpath("//span[contains(@class,'fr66n')]//button[contains(@class,'wpO6b')]")) > 0):
				btnLike = mybrowser.find_element_by_xpath("//span[contains(@class,'fr66n')]//button[contains(@class,'wpO6b')]")
				txtLike = mybrowser.find_element_by_xpath("//span[contains(@class,'fr66n')]//button[contains(@class,'wpO6b')]//div[contains(@class,'QBdPU')]//span//*[contains(@class,'_8-yf5')]").get_attribute('aria-label')
				kuduLike = "Like"
				gaLike = "Unlike"
				if txtLike == kuduLike:
					btnLike.click()
				if txtLike == gaLike:
					print("Posting Sudah Di Like")
					pass
				sleep(2)
			if(len(mybrowser.find_elements_by_xpath("//span[contains(@class,'fr66n')]//button[contains(@class,'wpO6b')]")) < 0):
				pass

			sleep(2)
			if(len(mybrowser.find_elements_by_class_name("coreSpriteRightPaginationArrow")) > 0):
				btnNext = mybrowser.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
				sleep(2)	
			if(len(mybrowser.find_elements_by_class_name("coreSpriteRightPaginationArrow")) < 0):
				pass
			sleep(2)
			
			# Klik NEXT POSTING
			prosesview = int((self.viewPost)+1)
			i=2
			while i < prosesview:
				
				print(Blue+"Proses Like Posting Ke-",i, ""+Reset+"")

				# Check LIKE
				if(len(mybrowser.find_elements_by_xpath("//span[contains(@class,'fr66n')]//button[contains(@class,'wpO6b')]")) > 0):
					btnLike = mybrowser.find_element_by_xpath("//span[contains(@class,'fr66n')]//button[contains(@class,'wpO6b')]")
					txtLike = mybrowser.find_element_by_xpath("//span[contains(@class,'fr66n')]//button[contains(@class,'wpO6b')]//div[contains(@class,'QBdPU')]//span//*[contains(@class,'_8-yf5')]").get_attribute('aria-label')
					kuduLike = "Like"
					gaLike = "Unlike"
					if txtLike == kuduLike:
						btnLike.click()
					if txtLike == gaLike:
						print("Posting Sudah Di Like")
						pass
					sleep(2)
				if(len(mybrowser.find_elements_by_xpath("//span[contains(@class,'fr66n')]//button[contains(@class,'wpO6b')]")) < 0):
					continue

				print ("Proses ke:", i, "   Telah dijalankan,"+Blue+"  DONE!!!"+Reset+"")
				sleep(5)
				
				if(len(mybrowser.find_elements_by_class_name("coreSpriteRightPaginationArrow")) > 0):
					btnNext = mybrowser.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
					sleep(2)	
				if(len(mybrowser.find_elements_by_class_name("coreSpriteRightPaginationArrow")) < 0):
					continue
				sleep(2)
				i=i+1
				sleep(2)	
			sleep(2)
			mybrowser.refresh()
		mybrowser.close()

