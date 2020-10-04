import keyboard

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

from time import sleep
import threading 
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
from progressbar import ProgressBar
from progress.bar import Bar
from alive_progress import alive_bar, show_bars, show_spinners, config_handler, showtime
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
class ORGID:
	def __init__(self):
		
		
		print ()
		print ("===============================================================")
		print("O R G A N I C  F O L L O W by ")
		result = pyfiglet.figlet_format("Circle - ID")
		print(result)
		print ("                                          -SANGBATOSAI | CODE5-")
		print ("         The Quieter You Become, The More You Are Able To Hear.")
		print ("                                                              -")
		print ("                                                    NGOPI ITEM.")
		print ("---------------------------------------------------------------")
		print ()
		
		print (" NOTE !!! MAX FOLLOW 7-13 follows/hour or 100-150 follows/day")
		print (" NOTE !!! MAX LIKE 700 to 1000 a day")

		self.idnya =           str(input(Reset+' [-] ID/Username    		: '+Green+''))
		self.jmlfollower =           float(input(Reset+' [-] Target Follow    		: '+Green+''))		
		self.viewer =           int(input(Reset+' [-] Jumlah Posting     	: '+Green+''))
		self.iUser = modulenya.modul_login.creditsPy.username
		self.iPass = modulenya.modul_login.creditsPy.password
		self.iUrl = modulenya.modul_login.creditsPy.url_profile

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
		iUrl = self.iUrl

		
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


	def cariFollowernya(self):
		mybrowser=self.mybrowser
		jml_follA=self.jmlfollower
		mybrowser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
		sleep(2)
		popupA = mybrowser.find_element_by_class_name('isgrP')
		
		last_hgt, hgt=0,1
		while last_hgt != hgt:
			last_hgt = hgt
			sleep(1)
			linkNama = popupA.find_elements_by_class_name('FPmhX')
			self.nama = [name.text for name in linkNama]
			#nama = self.nama[0: (int(jml_follA))]
			if len(self.nama)< jml_follA:
				hgt = self.mybrowser.execute_script("""
					arguments[0].scrollTo(0, arguments[0].scrollHeight);
					return arguments[0].scrollHeight;
					""", popupA)
				
		self.namas = self.nama[0: (int(jml_follA))]
		self.mybrowser.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button/div").click()

		print()	
		sleep(2)
		print("Proses Analisa Follower Potensial")
		print(Green+"Follower:")	
		print(self.namas, Reset)
		print(len(self.namas))
		return self.namas

	def ikutiFollowernya(self):
		mybrowser=self.mybrowser
		idnya=self.idnya
		iUrl = self.iUrl
		iUser = self.iUser
		
		for follower in self.namas:
			sleep(3)
			if follower == iUser:
				print()
				print("SKIP ACCOUNT")
				continue
				sleep(2)
			mybrowser.get("https://www.instagram.com/" + follower)
			sleep(2)
			print()
			print("Proses Organic Follow " + follower)
			sleep(3)
			
			config_handler.set_global(length=30, spinner='ball_scrolling')
			rangenya = range(1000)
			with alive_bar (len(rangenya), bar='blocks') as bar:
				for n in rangenya:
					if(len(mybrowser.find_elements_by_xpath("//button[contains(text(), 'Follow')]")) > 0):
						btn_follow = mybrowser.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()
						sleep(2)
				
					if(len(mybrowser.find_elements_by_xpath("//button[contains(text(), 'Follow')]")) < 0):
						pass
						sleep(2)
					
					if(len(mybrowser.find_elements_by_xpath("//*[contains(text(), 'No Posts Yet')]")) > 0):
						# If they're private, we can't see their follower list, so skip them
						print(Blue+"Akun Terdeteksi BELUM ADA POSTING"+Reset)
						continue
						sleep(2)
						
					if(len(mybrowser.find_elements_by_xpath("//*[contains(text(), 'This Account is Private')]")) > 0):
						# If they're private, we can't see their follower list, so skip them
						print(Blue+"Akun Terdeteksi PRIVATE"+Reset)
						continue
						sleep(2)
						
		
					# Klik TOP POSTING
					sleep(2)
					print("Membuka Top Posting " + follower)
					if(len(mybrowser.find_elements_by_class_name("eLAPa")) > 0):
						element2= mybrowser.find_element_by_class_name("eLAPa").click()
					if(len(mybrowser.find_elements_by_class_name("eLAPa")) < 0):
						print(Blue+"Akun Terdeteksi Belum ada Posting"+Reset)
						continue
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
						continue
					sleep(2)
					bar()
					
					
					
					# Klik NEXT POSTING
					prosesview = int((self.viewer)+1)
					i=2
					while i < prosesview:
						with alive_bar (len(rangenya), bar='blocks') as bar:
							for n in rangenya:
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
								mybrowser.refresh()
								bar()
					i+=1
				sleep(2)
				mybrowser.refresh()
					
				#mybrowser.close()
	



