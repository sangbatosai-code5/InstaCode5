import requests, sys, time, os, random
from random import randint
import keyboard
from time import sleep
import java

import pyfiglet


#MODULE IMPORT

import modulenya.modul_menu.banner_out
import modulenya.modul_menu.under
import modulenya.modul_menu.helpnya
from modulenya.modul_menu.helpnya import *

import modulenya.modul_comment.comm_id
import modulenya.modul_comment.comm_htag
from modulenya.modul_comment.comm_htag import HTAG

import modulenya.modul_like.like_htag
import modulenya.modul_like.like_id

import modulenya.modul_follow.foll_id
import modulenya.modul_follow.foll_htag
import modulenya.modul_follow.foll_htag2
import modulenya.modul_follow.foll_back
import modulenya.modul_follow.foll_unfollow
import modulenya.modul_follow.foll_blacklist

import modulenya.modul_organic.organic_circle_id
import modulenya.modul_organic.organic_htag
import modulenya.modul_organic.organic_htag2
import modulenya.modul_organic.xorganic_circle_idProxy
import modulenya.modul_organic.xorganic_htagProxy

import modulenya.modul_feedback.fback_Followers
import modulenya.modul_feedback.fback_FollowersB


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
class HeaderCustom(object):
	def __init__(self):
		self.print_logo()
		

	def print_logo(self): 
		clear = "\x1b[0m"
		colors = [36, 32, 34, 35, 31, 37]
		x = """
[Lets Build Your Own Code]
 ___           _               ____ ___  ____  _____ ____  
|_ _|_ __  ___| |_ __ _       / ___/ _ \|  _ \| ____| ___|
 | || '_ \/ __| __/ _` |_____| |  | | | | | | |  _| |___ \ 
 | || | | \__ \ || (_| |_____| |__| |_| | |_| | |___ ___) |
|___|_| |_|___/\__\__,_|      \____\___/|____/|_____|____/ 

GitHub.com/sangbatosai-code5                    
Development V.1.Aug2020       
    """
		for N, line in enumerate(x.split("\n")):
			sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
			time.sleep(0.05)


headernya=HeaderCustom()
print (Reset+"         The Quieter You Become, The More You Are Able To Hear."+Blue+"")
print ("                                          -SANGBATOSAI | CODE5-")
print ("                                                    NGOPI ITEM.")
print ("---------------------------------------------------------------")
print ()




def pilihanmenu(self):
	try:
		
		sleep(1)
		print(Green+'M E N U | ORGANIC METHOD |INSTA-Code5')
		print(Green+'Pilihan berdasarkan Algorithma Method')
		print()
		pilihan = input ("""[-] COMMENT METHOD [-]
     [1]  COMMENT BY HASHTAG         [Comment Only]
     [2]  COMMENT BY USERNAME        [Comment Only]

[-] LIKE METHOD [-]
     [3]  LIKE BY HASHTAG            [Like Only]
     [4]  LIKE BY USERNAME           [Like Only]
	     
[-] FOLLOW - UNFOLLOW METHOD [-]
     [5]  FOLLOW BY ID               [CIRCLE Method FAST Follow]
     [6]  FOLLOW BY HASHTAG          [Follow-Like-Comment]
     [7]  FOLLOW BY HASHTAG-2        [Follow-Like]
     [8]  FOLLBACK                   [Follow Back]
     [9]  UNFOLLOW                   [Unfollow ALL Followers]
     [10] UNFOLLOW BLACKLIST         [Unfollow FollBlack!]
	     
[-] ORGANIC METHOD [-]
     [11] ORGANIC BY ID              [CIRCLE METHOD]
     [12] ORGANIC BY HASHTAG         [CIRCLE METHOD-COMMENT]
     [13] ORGANIC BY HASHTAG II      [CIRCLE METHOD-LIKE]
     [14] X-ORGANIC BY ID            [Proxy Chains]
     [15] X-ORGANIC BY HASHTAG       [Proxy Chains]
	     
[-] FEEDBACK METHOD [-]
     [16] FeedBack Post Followers I  [Like Their Post]
     [17] FeedBack Post Followers II [Like-Comment Their Post]
     [18] FeedBack Story Followers   [Like Their Post]



[-] S E T T I N G [-]
     [97] HELP                      [Rules 0f Instagram]
     [98] SETTING                   [..........]
     [99] Exit/Quit 
		
Pilihan 	:""")
	
		if pilihan == "1":
			print ("Method HASHTAG dipilih")
			pilih_hashtag()
			print()
			sleep(2)

		elif pilihan == "2":
			print ("Method ID/Username dipilih")
			pilih_id()
			print()
			sleep(2)

		if pilihan == "3":
			print ("Method ONLY LIKE- by Hashtag dipilih")
			pilih_likehashtag()
			print()
			sleep(2)

		elif pilihan == "4":
			print ("Method ONLY LIKE- by ID/Username dipilih")
			pilih_likeid()
			print()
			sleep(2)

		elif pilihan == "5":
			print ("Method Follow by ID/Username | Circle ID")
			pilih_follow_id()
			print()
			sleep(2)

		elif pilihan == "6":
			print ("Method Follow by HashTag Posting")
			pilih_follow_htag()
			print()
			sleep(2)

		elif pilihan == "7":
			print ("Method Follow by HashTag Posting II")
			pilih_follow_htag2()
			print()
			sleep(2)

		elif pilihan == "8":
			print ("Method FollBack")
			pilih_follow_back()
			print()
			sleep(2)
	
		elif pilihan == "9":
			print ("Method UnFollow ALL")
			pilih_unfollow()
			print()
			sleep(2)
	
		elif pilihan == "10":
			print ("Method UnFollow Blacklist")
			pilih_unfollowBlacklist()
			print()
			sleep(2)
	
		elif pilihan == "11":
			print ("Method Organic by ID")
			pilih_org_id()
			print()
			sleep(2)
	
		elif pilihan == "12":
			print ("Method Organic by Hashtag - COMMENT")
			pilih_org_htag()
			print()
			sleep(2)
	
	
		elif pilihan == "13":
			print ("Method Organic by Hashtag - LIKE")
			pilih_org_htag2()
			print()
			sleep(2)
	
		elif pilihan == "14":
			print ("Method Organic by ID Using ProxyChains")
			pilih_xorg_id()
			print()
			sleep(2)
	
		elif pilihan == "15":
			print ("Method Organic by Hashtag Using ProxyChains")
			pilih_xorg_htag()
			print()
			sleep(2)
	
	
		elif pilihan == "16":
			print ("Method Feedback Followers Post")
			pilih_feedback_A()
			print()
			sleep(2)
	
		elif pilihan == "17":
			print ("Method Feedback Followers Post")
			pilih_feedback_B()
			print()
			sleep(2)
	
		elif pilihan == "97":
			print ("HELP")
			pilih_help()
			print()
			sleep(2)
	
	
		elif pilihan == "98":
			print ("SETTING")
			pilih_setting()
			print()
			sleep(2)
	
		elif pilihan == "99":
			 modulenya.modul_menu.banner_out.selesai()
	
		else:
			print()
			print (Red+"[ S A L A H !!! ]" +Reset+" Masukan Sesuai Pilihan Diatas !!! ]"+Reset)
			print()
			print ("---------------------------------------------------------------")
			pilihanmenu(1)
	
	

	except KeyboardInterrupt:
		print()
		sleep(1)
		print ("---------------------------------------------------------------")
		print (Red+"\n[KEYBOARD INTERUPTED!!!!]")
		print ("[Keterangan: PROGRAM DIHENTIKAN SECARA MANUAL | FORCED CLOSED]"+Reset)
		print()
		modulenya.modul_menu.banner_out.selesai()
		print()
		exit()
		
def pilih_hashtag():
	print("C O M M E N T  by H A S H T A G ")
	pHastag = modulenya.modul_comment.comm_htag.HTAG()
	pHastag.loginakun()
	pHastag.mencari()
	pHastag.klik_top_posting()
	pHastag.klik_next_posting()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_id():
	print("C O M M E N T  by U S E R N A M E ")
	pID= modulenya.modul_comment.comm_id.HID()
	pID.loginakun()
	pID.mencari()
	pID.klik_top_posting()
	pID.klik_next_posting()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)
		
def pilih_likehashtag():
	print("L I K E  by H A S H T A G ")
	pHastag = modulenya.modul_like.like_htag.LTAG()
	pHastag.loginakun()
	pHastag.mencari()
	pHastag.klik_top_posting()
	pHastag.klik_next_posting()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_likeid():
	print("L I K E  by U S E R N A M E ")
	pID= modulenya.modul_like.like_id.LID()
	pID.loginakun()
	pID.mencari()
	pID.klik_top_posting()
	pID.klik_next_posting()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_follow_id():
	pFollid = modulenya.modul_follow.foll_id.FID()

	print("BOOST FOLLOWER by U S E R N A M E | CIRCLE METHOD")
	pFollid.loginakun()
	pFollid.mencari()
	pFollid.cek_followernya()
	#pFollid.ikutiFollowernya(1)
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_follow_htag():
	pFtag = modulenya.modul_follow.foll_htag.FTAG()
	print("BOOST FOLLOWER by H A S H T A G ")
	pFtag.loginakun()
	pFtag.mencari()
	pFtag.klik_top_posting()
	pFtag.klik_next_posting()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_follow_htag2():
	pFtag = modulenya.modul_follow.foll_htag2.FTAG()
	print("BOOST FOLLOWER by H A S H T A G ")
	pFtag.loginakun()
	pFtag.mencari()
	pFtag.klik_top_posting()
	pFtag.klik_next_posting()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_follow_back():
	pFback = modulenya.modul_follow.foll_back.FLBACK()
	print("FOLLOW BACK Our FOLLOWER")
	pFback.loginakun()
	pFback.mencari()
	pFback.daftar_belumFollBack()
	pFback.menupilih_follback()
	pFback.menupilihFollBack_y()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_unfollow():
	pUfoll = modulenya.modul_follow.foll_unfollow.FLUN()
	print("UNFOLLOW ALL FOLLOWER")
	pUfoll.loginakun()
	pUfoll.mencari()	
	pUfoll.cek_following()	
	print()
	print ("---------------------------------------------------------------")
	sleep(3)
	pilihanmenu(1)
	
def pilih_unfollowBlacklist():
	pFblack = modulenya.modul_follow.foll_blacklist.FLBLACK()
	print("UNFOLLOW Our BLACKLIST FOLLOWER")
	pFblack.loginakun()
	pFblack.mencari()
	pFblack.daftar_Blacklistfollower()
	pFblack.menupilih_follblack()
	pFblack.menupilihFollBlack_y()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_org_id():
	pOrgFollid = modulenya.modul_organic.organic_circle_id.ORGID()
	print("ORGANIC by U S E R N A M E | CIRCLE METHOD")
	pOrgFollid.loginakun()
	pOrgFollid.mencari()
	pOrgFollid.cariFollowernya()
	pOrgFollid.ikutiFollowernya()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_org_htag():
	pOrgFtag = modulenya.modul_organic.organic_htag.ORGTAG()
	print("ORGANIC by H A S H T A G ")
	pOrgFtag.loginakun()
	pOrgFtag.mencari()
	pOrgFtag.daftarCommentator()
	pOrgFtag.prosesFollow()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_org_htag2():
	pOrgFtag = modulenya.modul_organic.organic_htag2.ORGTAG()
	print("ORGANIC by H A S H T A G II")
	pOrgFtag.loginakun()
	pOrgFtag.mencari()
	#pOrgFtag.cekliker()
	pOrgFtag.daftarLiker()
	pOrgFtag.prosesFollow()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_xorg_id():
	pXorgFollid = modulenya.modul_organic.xorganic_circle_idProxy.XORGID()
	print("XORGANIC by U S E R N A M E | CIRCLE METHOD")
	pXorgFollid.loginakun()
	pXorgFollid.mencari()
	pXorgFollid.cariFollowernya()
	pXorgFollid.ikutiFollowernya()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_xorg_htag():
	pXorgFtag = modulenya.modul_organic.xorganic_htagProxy.XORGTAG()
	print("XORGANIC by H A S H T A G ")
	pXorgFtag.loginakun()
	pXorgFtag.mencari()
	pXorgFtag.daftarCommentator()
	pXorgFtag.prosesFollow()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_feedback_A():
	pFBFoll = modulenya.modul_feedback.fback_Followers.FeedBack()
	print("Feedback Followers Post - L I K E")
	pFBFoll.loginakun()
	pFBFoll.mencari()
	pFBFoll.daftar_FollowersIng()
	pFBFoll.prosesFeedback()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

def pilih_feedback_B():
	pFBFollB = modulenya.modul_feedback.fback_FollowersB.FeedBack()
	print("Feedback Followers Post - L I K E  & C O M M E N T")
	pFBFollB.loginakun()
	pFBFollB.mencari()
	pFBFollB.daftar_FollowersIng()
	pFBFollB.prosesFeedback()
	print()
	print ("---------------------------------------------------------------")
	pilihanmenu(1)

#===========================================================================================
def pilih_setting():
	print()
	sleep(5)
	pSet = modulenya.modul_menu.under.HeaderUnderConst()
	print("MASIH DALAM PENGEMBANGAN")
	print()
	print ("---------------------------------------------------------------")
	sleep(3)
	pilihanmenu(1)
	
def pilih_help():
	print()
	sleep(1)
	pSet = modulenya.modul_menu.helpnya.HeaderHelp()
	print("Kembali ke Menu Utama")
	print()
	print ("---------------------------------------------------------------")
	sleep(1)
	pilihanmenu(1)

def pilih_underconstructions():
	print()
	sleep(5)
	pSet = modulenya.modul_menu.under.HeaderUnderConst()
	print("MASIH DALAM PENGEMBANGAN")
	print()
	print ("---------------------------------------------------------------")
	sleep(3)
	pilihanmenu(1)


print (Reset+"")
#print ("===============================================================")	

pilihanmenu(0)



