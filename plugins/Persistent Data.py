import os
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWebEngineCore import *

toolTip = "Store persistent\nBrowser data and\nthe cache."

def main(HolyGrail):
	if not os.path.isdir(os.getcwd()+"\\Data"):
		os.mkdir(os.getcwd()+"\\Data")
	#add check for off the record, then disable
	HolyGrail.browser.profile = QWebEngineProfile("Monty")
	HolyGrail.browser.profile.setPersistentStoragePath(os.getcwd()+"\\Data")
	HolyGrail.browser.profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies)
	
#HolyGrail.browser.profile.setCachePath(os.getcwd()+"\\Data")

def end(HolyGrail):
	#replace by enabling off the record
	HolyGrail.browser.profile = QWebEngineProfile.defaultProfile()
	