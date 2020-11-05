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
class FTAG:
	def __init__(self):
		
		
		print ()
		print ("===============================================================")
		print("F O L L O W - L I K E")
		result = pyfiglet.figlet_format("HashTag")
		print(result)
		print ("                                          -SANGBATOSAI | CODE5-")
		print ("         The Quieter You Become, The More You Are Able To Hear.")
		print ("                                                              -")
		print ("                                                    NGOPI ITEM.")
		print ("---------------------------------------------------------------")
		print ()
		
		print (" NOTE !!! MAX FOLLOW 7-13 follows/hour or 100-150 follows/day")
		print (" NOTE !!! MAX LIKE 700 to 1000 a day")
		self.hashtagnya =           str(input(Reset+' [-] Hashtag    		: '+Green+''))
		self.viewer =           int(input(Reset+' [-] Jumlah Posting     	: '+Green+''))
		
		self.iUser = modulenya.modul_login.creditsPy.username
		self.iPass = modulenya.modul_login.creditsPy.password
		
		
		
		print (Reset+"")
		print ()
		print ("===============================================================")
		print ()
		print ('Proses Dimulai ...')
		print ()
	    

	def loginakun(self):
		self.driver_path = "WebDriver/geckodriver"
		self.mybrowser = webdriver.Firefox(executable_path=self.driver_path)
		mybrowser=self.mybrowser
		mybrowser.implicitly_wait(8)
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
		hashtagnya=self.hashtagnya
		print("Proses Mencari sesuai hashtag #"+hashtagnya+"")
		# Searching hashtag
		element1 = mybrowser.get("https://www.instagram.com/explore/tags/"+hashtagnya+"/")
		sleep(2)
		for i in range(1, 1):
			mybrowser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			sleep(2)
	
	def klik_top_posting(self):
		mybrowser=self.mybrowser
		
		
		# Klik TOP POSTING
		sleep(2)
		print("Membuka Top Posting")
		element2= mybrowser.find_element_by_class_name("eLAPa").click()
		sleep(3)
		
		# Check Follow
		if(len(mybrowser.find_elements_by_xpath("//button[contains(text(), 'Follow')]")) > 0):
			mybrowser.find_element_by_xpath("//div[contains(@class,'bY2yH')]").click()
		
		if(len(mybrowser.find_elements_by_xpath("//*[contains(text(), 'Unfollow')]")) > 0):
			mybrowser.find_element_by_xpath("//button[contains(.,'Cancel')]").click()
			sleep(2)
		else:
			pass 
			sleep(2)

		# Check LIKE
		btnLike = mybrowser.find_element_by_xpath("//span[contains(@class,'fr66n')]//button[contains(@class,'wpO6b')]")
		txtLike = mybrowser.find_element_by_xpath("//span[contains(@class,'fr66n')]//button[contains(@class,'wpO6b')]//div[contains(@class,'QBdPU')]//span//*[contains(@class,'_8-yf5')]").get_attribute('aria-label')
		kuduLike = "Like"
		gaLike = "Unlike"

		sleep(2)
		if txtLike == kuduLike:
			btnLike.click()
			sleep(2)
			
		if txtLike == gaLike:
			print("Posting Sudah Di Like")
			pass

		sleep(2)
		mybrowser.find_element_by_class_name("coreSpriteRightPaginationArrow").click()	
		sleep(2)

	def klik_next_posting(self):
		try:
			mybrowser=self.mybrowser
			prosesview = int((self.viewer)+1)
			i=2
			while i < prosesview:
				# Klik NEXT
				print(Blue+"Proses Like-Follow Posting Ke-",i, ""+Reset+"")
				
				
				# Check Follow
				sleep(3)
				if(len(mybrowser.find_elements_by_xpath("//button[contains(text(), 'Follow')]")) > 0):
					mybrowser.find_element_by_xpath("//div[contains(@class,'bY2yH')]").click()
				
				if(len(mybrowser.find_elements_by_xpath("//*[contains(text(), 'Unfollow')]")) > 0):
					mybrowser.find_element_by_xpath("//button[contains(.,'Cancel')]").click()
					sleep(2)
				else:
					pass 
					sleep(2)
		
				# Check LIKE
				btnLike = mybrowser.find_element_by_xpath("//span[contains(@class,'fr66n')]//button[contains(@class,'wpO6b')]")
				txtLike = mybrowser.find_element_by_xpath("//span[contains(@class,'fr66n')]//button[contains(@class,'wpO6b')]//div[contains(@class,'QBdPU')]//span//*[contains(@class,'_8-yf5')]").get_attribute('aria-label')
				kuduLike = "Like"
				gaLike = "Unlike"
		
				sleep(2)
				if txtLike == kuduLike:
					btnLike.click()
					sleep(2)
					
				if txtLike == gaLike:
					print("Posting Sudah Di Like")
					pass


				print ("Proses ke:", i, "   Telah dijalankan,"+Blue+"  DONE!!!"+Reset+"")
				sleep(5)
				
				mybrowser.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
				sleep(2)
				i=i+1
				
				sleep(2)
		
		except AttributeError:
			print("There is no Such Attribute, kosong value")
				
		except Exception as e: 
			print ()
			print("   \tPeriksa bagian Code: \n\t",e,)
			print (Red+"===============================================================")
			print (Green+"      [LINK tidak diketemukan, silahkan cek ALGORITMA!]")
			print ()
			print ("                      CEK LINK TARGET!!!!")
			print (Red+"===============================================================")
			print ()
			print ()
			pass
			
		else:
			sleep(2)
			print (Green+"---------------------------------------------------------------")
			print ()
			print ("                [PROSES TELAH BERJALAN SEMUA]")
			print ("                      [MENUTUP BROWSER]")
			print ()
			print ("---------------------------------------------------------------")
			sleep(1)
		
		finally:
			print ()
			print ()
			print (""+Green+"===============================================================")
			print ("===============================================================")
			print ()
			print ()
			print ()
			sleep(2)
			mybrowser.close()	
				
				
				
				
				
				

		
		
		
		
		
		
		
		
		
		
		
