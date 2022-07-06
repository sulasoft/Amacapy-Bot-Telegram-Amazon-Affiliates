import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.uic import loadUi
import os
import io
from io import open
from time import sleep
import time
from datetime import date, timedelta, datetime
import requests
import requests_cache
import webbrowser
from pyshorteners import Shortener
from threading import Thread
import threading
from bs4 import BeautifulSoup
import linecache as lc
import resources


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		loadUi("AmacapyUI.ui", self)
		
		self.setWindowTitle("Amacapy")
		self.setWindowIcon(QtGui.QIcon('logo_amacapy.ico'))

		self.thread = {}

		# Settings Screen
		self.returnButton.clicked.connect(self.closeSettingsControl)
		self.saveSettingsButton.clicked.connect(self.saveSettings)
		self.savedSettingsText.hide()
		self.settingsFrame.hide()
		self.closeSettingsButton.hide()

		# Product To Publish Screen

		self.deleteProduct1Button.clicked.connect(self.deleteProduct1)
		self.deleteProduct2Button.clicked.connect(self.deleteProduct2)
		self.deleteProduct3Button.clicked.connect(self.deleteProduct3)
		self.deleteProduct4Button.clicked.connect(self.deleteProduct4)
		self.deleteProduct5Button.clicked.connect(self.deleteProduct5)
		self.deleteProduct6Button.clicked.connect(self.deleteProduct6)
		self.deleteProduct7Button.clicked.connect(self.deleteProduct7)
		self.deleteProduct8Button.clicked.connect(self.deleteProduct8)
		self.deleteProduct9Button.clicked.connect(self.deleteProduct9)
		self.deleteProduct10Button.clicked.connect(self.deleteProduct10)
		self.deleteProduct11Button.clicked.connect(self.deleteProduct11)
		self.deleteProduct12Button.clicked.connect(self.deleteProduct12)

		self.publishButton.clicked.connect(self.publishProducts)
		self.textPublishedQuantity.hide()
		self.stopPublishButton.hide()
		self.stopPublishButton.clicked.connect(self.stopPublish)

		self.seePublish1.clicked.connect(self.seeProductsPublish1)
		self.seePublish2.clicked.connect(self.seeProductsPublish2)
		self.seePublish3.clicked.connect(self.seeProductsPublish3)
		self.seePublish4.clicked.connect(self.seeProductsPublish4)
		self.seePublish5.clicked.connect(self.seeProductsPublish5)
		self.seePublish6.clicked.connect(self.seeProductsPublish6)
		self.seePublish7.clicked.connect(self.seeProductsPublish7)
		self.seePublish8.clicked.connect(self.seeProductsPublish8)
		self.seePublish9.clicked.connect(self.seeProductsPublish9)
		self.seePublish10.clicked.connect(self.seeProductsPublish10)
		self.seePublish11.clicked.connect(self.seeProductsPublish11)
		self.seePublish12.clicked.connect(self.seeProductsPublish12)


		# Search Result Screen

		self.deleteResult1Button.clicked.connect(self.deleteResult1)
		self.deleteResult2Button.clicked.connect(self.deleteResult2)
		self.deleteResult3Button.clicked.connect(self.deleteResult3)
		self.deleteResult4Button.clicked.connect(self.deleteResult4)
		self.deleteResult5Button.clicked.connect(self.deleteResult5)
		self.deleteResult6Button.clicked.connect(self.deleteResult6)
		self.deleteResult7Button.clicked.connect(self.deleteResult7)
		self.deleteResult8Button.clicked.connect(self.deleteResult8)
		self.deleteResult9Button.clicked.connect(self.deleteResult9)
		self.deleteResult10Button.clicked.connect(self.deleteResult10)
		self.deleteResult11Button.clicked.connect(self.deleteResult11)
		self.deleteResult12Button.clicked.connect(self.deleteResult12)

		self.addProductsButton.clicked.connect(self.addProductsToPublish)
		self.showProductsButton.clicked.connect(self.showProductsToPublishScreen)

		self.closeProductsToPublishButton.hide()
		self.closeSearchResultButton.hide()

		self.textAddedProducts.hide() # Message of products successfully added
		self.textFullCapacity.hide() # Message of capacity full of products

		self.seeResult1Button.clicked.connect(self.seeProductsResult1)
		self.seeResult2Button.clicked.connect(self.seeProductsResult2)
		self.seeResult3Button.clicked.connect(self.seeProductsResult3)
		self.seeResult4Button.clicked.connect(self.seeProductsResult4)
		self.seeResult5Button.clicked.connect(self.seeProductsResult5)
		self.seeResult6Button.clicked.connect(self.seeProductsResult6)
		self.seeResult7Button.clicked.connect(self.seeProductsResult7)
		self.seeResult8Button.clicked.connect(self.seeProductsResult8)
		self.seeResult9Button.clicked.connect(self.seeProductsResult9)
		self.seeResult10Button.clicked.connect(self.seeProductsResult10)
		self.seeResult11Button.clicked.connect(self.seeProductsResult11)
		self.seeResult12Button.clicked.connect(self.seeProductsResult12)

		# Main Screen

		self.searchButton.clicked.connect(self.searchProduct)
		self.sulasoftCR.clicked.connect(self.openSulasoftWeb)

		self.openSearchResultButton.clicked.connect(self.showResultsScreen)
		self.closeSearchResultButton.clicked.connect(self.closeResultScreen)
		self.openProductsToPublishButton.clicked.connect(self.showProductsToPublishScreen)
		self.closeProductsToPublishButton.clicked.connect(self.closeProductsToPublishScreen)
		self.stopButton.clicked.connect(self.stopProcess)

		self.openSettingsButton.clicked.connect(self.openSettingsControl)
		self.closeSettingsButton.clicked.connect(self.closeSettingsControl)

		self.searchBarFrame.hide()

		self.LoadSettings()

		self.searchResultScreen.hide()
		self.productsPublishScreen.hide()
		self.showProductsButton.hide()



	def stopProcess(self):
		self.thread[1].stop()
		self.searchBarFrame.hide()
		self.searchFrame.show()

	def stopPublish(self):
		self.thread[1].stop()
		self.publishButton.show()
		self.textPublishEvery.show()
		self.textTelegramMinutes.show()
		self.timePublish.show()
		self.stopPublishButton.hide()
		self.textPublishedQuantity.hide()
		self.closeProductsToPublishScreen()


	def openSulasoftWeb(self):
		webbrowser.open("https://sulasoft.com")

	def openSettingsControl(self):
		self.settingsFrame.show()
		self.openSettingsButton.hide()
		self.closeSettingsButton.show()

		self.productsPublishScreen.hide()
		self.searchResultScreen.hide()

		self.closeSearchResultButton.hide()
		self.openSearchResultButton.show()

		self.closeProductsToPublishButton.hide()
		self.openProductsToPublishButton.show()
	

	def closeSettingsControl(self):
		self.settingsFrame.hide()
		self.openSettingsButton.show()
		self.closeSettingsButton.hide()
		self.savedSettingsText.hide()

	def saveSettings(self):

		fields = [self.amazonid.text(), self.telegramToken.text(), self.chatID.text()]

		if "" in fields:
			QMessageBox.information(self, "Error", "You cannot leave fields blank.")
			conf_p = ""
			f = open ('config.txt','w')
			f.write(str(conf_p))
			f.close()
			self.savedSettingsText.hide()

		elif self.chatID.text().startswith("@") == False:
			QMessageBox.information(self, "Error", 'You must add the "@" to the Chat ID.')
			conf_p = ""
			f = open ('config.txt','w')
			f.write(str(conf_p))
			f.close()
			self.savedSettingsText.hide()

		else:	
			conf_p = self.amazonid.text() + "\n" + self.telegramToken.text() + "\n" + self.chatID.text()
		
			f = open ('config.txt','w')
			f.write(str(conf_p))
			f.close()

			self.savedSettingsText.show()

	def LoadSettings(self):
		f = open ('config.txt')
		readLines = f.read().splitlines()
		f.close()

		if len(readLines) == 0:
			self.amazonid.setText("") 
			self.telegramToken.setText("")
			self.chatID.setText("")
		else:
			self.amazonid.setText(readLines[0]) 
			self.telegramToken.setText(readLines[1])
			self.chatID.setText(readLines[2])

	def showResultsScreen(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		self.titleResult1.hide()
		self.priceResult1.hide()
		self.deleteResult1Button.hide()
		self.nro1.hide()
		self.seeResult1Button.hide()

		self.titleResult2.hide()
		self.priceResult2.hide()
		self.deleteResult2Button.hide()
		self.nro2.hide()
		self.seeResult2Button.hide()

		self.titleResult3.hide()
		self.priceResult3.hide()
		self.deleteResult3Button.hide()
		self.nro3.hide()
		self.seeResult3Button.hide()

		self.titleResult4.hide()
		self.priceResult4.hide()
		self.deleteResult4Button.hide()
		self.nro4.hide()
		self.seeResult4Button.hide()

		self.titleResult5.hide()
		self.priceResult5.hide()
		self.deleteResult5Button.hide()
		self.nro5.hide()
		self.seeResult5Button.hide()

		self.titleResult6.hide()
		self.priceResult6.hide()
		self.deleteResult6Button.hide()
		self.nro6.hide()
		self.seeResult6Button.hide()

		self.titleResult7.hide()
		self.priceResult7.hide()
		self.deleteResult7Button.hide()
		self.nro7.hide()
		self.seeResult7Button.hide()

		self.titleResult8.hide()
		self.priceResult8.hide()
		self.deleteResult8Button.hide()
		self.nro8.hide()
		self.seeResult8Button.hide()

		self.titleResult9.hide()
		self.priceResult9.hide()
		self.deleteResult9Button.hide()
		self.nro9.hide()
		self.seeResult9Button.hide()

		self.titleResult10.hide()
		self.priceResult10.hide()
		self.deleteResult10Button.hide()
		self.nro10.hide()
		self.seeResult10Button.hide()

		self.titleResult11.hide()
		self.priceResult11.hide()
		self.deleteResult11Button.hide()
		self.nro11.hide()
		self.seeResult11Button.hide()

		self.titleResult12.hide()
		self.priceResult12.hide()
		self.deleteResult12Button.hide()
		self.nro12.hide()
		self.seeResult12Button.hide()

		if len(_line) == 3:
			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult1.show()
			self.priceResult1.show()
			self.deleteResult1Button.show()
			self.nro1.show()
			self.seeResult1Button.show()

		if len(_line) == 6:
			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult1.show()
			self.priceResult1.show()
			self.deleteResult1Button.show()
			self.nro1.show()
			self.seeResult1Button.show()

			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult2.show()
			self.priceResult2.show()
			self.deleteResult2Button.show()
			self.nro2.show()
			self.seeResult2Button.show()

		if len(_line) == 9:
			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult1.show()
			self.priceResult1.show()
			self.deleteResult1Button.show()
			self.nro1.show()
			self.seeResult1Button.show()

			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult2.show()
			self.priceResult2.show()
			self.deleteResult2Button.show()
			self.nro2.show()
			self.seeResult2Button.show()

			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult3.show()
			self.priceResult3.show()
			self.deleteResult3Button.show()
			self.nro3.show()
			self.seeResult3Button.show()

		if len(_line) == 12:
			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult1.show()
			self.priceResult1.show()
			self.deleteResult1Button.show()
			self.nro1.show()
			self.seeResult1Button.show()

			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult2.show()
			self.priceResult2.show()
			self.deleteResult2Button.show()
			self.nro2.show()
			self.seeResult2Button.show()

			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult3.show()
			self.priceResult3.show()
			self.deleteResult3Button.show()
			self.nro3.show()
			self.seeResult3Button.show()

			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult4.show()
			self.priceResult4.show()
			self.deleteResult4Button.show()
			self.nro4.show()
			self.seeResult4Button.show()

		if len(_line) == 15:
			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult1.show()
			self.priceResult1.show()
			self.deleteResult1Button.show()
			self.nro1.show()
			self.seeResult1Button.show()

			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult2.show()
			self.priceResult2.show()
			self.deleteResult2Button.show()
			self.nro2.show()
			self.seeResult2Button.show()

			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult3.show()
			self.priceResult3.show()
			self.deleteResult3Button.show()
			self.nro3.show()
			self.seeResult3Button.show()

			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult4.show()
			self.priceResult4.show()
			self.deleteResult4Button.show()
			self.nro4.show()
			self.seeResult4Button.show()

			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult5.show()
			self.priceResult5.show()
			self.deleteResult5Button.show()
			self.nro5.show()
			self.seeResult5Button.show()


		if len(_line) == 18:
			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult1.show()
			self.priceResult1.show()
			self.deleteResult1Button.show()
			self.nro1.show()
			self.seeResult1Button.show()

			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult2.show()
			self.priceResult2.show()
			self.deleteResult2Button.show()
			self.nro2.show()
			self.seeResult2Button.show()

			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult3.show()
			self.priceResult3.show()
			self.deleteResult3Button.show()
			self.nro3.show()
			self.seeResult3Button.show()

			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult4.show()
			self.priceResult4.show()
			self.deleteResult4Button.show()
			self.nro4.show()
			self.seeResult4Button.show()

			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult5.show()
			self.priceResult5.show()
			self.deleteResult5Button.show()
			self.nro5.show()
			self.seeResult5Button.show()

			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult6.show()
			self.priceResult6.show()
			self.deleteResult6Button.show()
			self.nro6.show()
			self.seeResult6Button.show()

		if len(_line) == 21:
			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult1.show()
			self.priceResult1.show()
			self.deleteResult1Button.show()
			self.nro1.show()
			self.seeResult1Button.show()

			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult2.show()
			self.priceResult2.show()
			self.deleteResult2Button.show()
			self.nro2.show()
			self.seeResult2Button.show()

			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult3.show()
			self.priceResult3.show()
			self.deleteResult3Button.show()
			self.nro3.show()
			self.seeResult3Button.show()

			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult4.show()
			self.priceResult4.show()
			self.deleteResult4Button.show()
			self.nro4.show()
			self.seeResult4Button.show()

			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult5.show()
			self.priceResult5.show()
			self.deleteResult5Button.show()
			self.nro5.show()
			self.seeResult5Button.show()

			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult6.show()
			self.priceResult6.show()
			self.deleteResult6Button.show()
			self.nro6.show()
			self.seeResult6Button.show()

			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult7.show()
			self.priceResult7.show()
			self.deleteResult7Button.show()
			self.nro7.show()
			self.seeResult7Button.show()

		if len(_line) == 24:
			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult1.show()
			self.priceResult1.show()
			self.deleteResult1Button.show()
			self.nro1.show()
			self.seeResult1Button.show()

			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult2.show()
			self.priceResult2.show()
			self.deleteResult2Button.show()
			self.nro2.show()
			self.seeResult2Button.show()

			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult3.show()
			self.priceResult3.show()
			self.deleteResult3Button.show()
			self.nro3.show()
			self.seeResult3Button.show()

			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult4.show()
			self.priceResult4.show()
			self.deleteResult4Button.show()
			self.nro4.show()
			self.seeResult4Button.show()

			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult5.show()
			self.priceResult5.show()
			self.deleteResult5Button.show()
			self.nro5.show()
			self.seeResult5Button.show()

			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult6.show()
			self.priceResult6.show()
			self.deleteResult6Button.show()
			self.nro6.show()
			self.seeResult6Button.show()

			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult7.show()
			self.priceResult7.show()
			self.deleteResult7Button.show()
			self.nro7.show()
			self.seeResult7Button.show()

			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult8.show()
			self.priceResult8.show()
			self.deleteResult8Button.show()
			self.nro8.show()
			self.seeResult8Button.show()

		if len(_line) == 27:
			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult1.show()
			self.priceResult1.show()
			self.deleteResult1Button.show()
			self.nro1.show()
			self.seeResult1Button.show()

			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult2.show()
			self.priceResult2.show()
			self.deleteResult2Button.show()
			self.nro2.show()
			self.seeResult2Button.show()

			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult3.show()
			self.priceResult3.show()
			self.deleteResult3Button.show()
			self.nro3.show()
			self.seeResult3Button.show()

			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult4.show()
			self.priceResult4.show()
			self.deleteResult4Button.show()
			self.nro4.show()
			self.seeResult4Button.show()

			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult5.show()
			self.priceResult5.show()
			self.deleteResult5Button.show()
			self.nro5.show()
			self.seeResult5Button.show()

			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult6.show()
			self.priceResult6.show()
			self.deleteResult6Button.show()
			self.nro6.show()
			self.seeResult6Button.show()

			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult7.show()
			self.priceResult7.show()
			self.deleteResult7Button.show()
			self.nro7.show()
			self.seeResult7Button.show()

			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult8.show()
			self.priceResult8.show()
			self.deleteResult8Button.show()
			self.nro8.show()
			self.seeResult8Button.show()

			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult9.show()
			self.priceResult9.show()
			self.deleteResult9Button.show()
			self.nro9.show()
			self.seeResult9Button.show()

		if len(_line) == 30:
			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult1.show()
			self.priceResult1.show()
			self.deleteResult1Button.show()
			self.nro1.show()
			self.seeResult1Button.show()

			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult2.show()
			self.priceResult2.show()
			self.deleteResult2Button.show()
			self.nro2.show()
			self.seeResult2Button.show()

			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult3.show()
			self.priceResult3.show()
			self.deleteResult3Button.show()
			self.nro3.show()
			self.seeResult3Button.show()

			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult4.show()
			self.priceResult4.show()
			self.deleteResult4Button.show()
			self.nro4.show()
			self.seeResult4Button.show()

			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult5.show()
			self.priceResult5.show()
			self.deleteResult5Button.show()
			self.nro5.show()
			self.seeResult5Button.show()

			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult6.show()
			self.priceResult6.show()
			self.deleteResult6Button.show()
			self.nro6.show()
			self.seeResult6Button.show()

			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult7.show()
			self.priceResult7.show()
			self.deleteResult7Button.show()
			self.nro7.show()
			self.seeResult7Button.show()

			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult8.show()
			self.priceResult8.show()
			self.deleteResult8Button.show()
			self.nro8.show()
			self.seeResult8Button.show()

			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult9.show()
			self.priceResult9.show()
			self.deleteResult9Button.show()
			self.nro9.show()
			self.seeResult9Button.show()

			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult10.show()
			self.priceResult10.show()
			self.deleteResult10Button.show()
			self.nro10.show()
			self.seeResult10Button.show()

		if len(_line) == 33:
			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult1.show()
			self.priceResult1.show()
			self.deleteResult1Button.show()
			self.nro1.show()
			self.seeResult1Button.show()

			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult2.show()
			self.priceResult2.show()
			self.deleteResult2Button.show()
			self.nro2.show()
			self.seeResult2Button.show()

			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult3.show()
			self.priceResult3.show()
			self.deleteResult3Button.show()
			self.nro3.show()
			self.seeResult3Button.show()

			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult4.show()
			self.priceResult4.show()
			self.deleteResult4Button.show()
			self.nro4.show()
			self.seeResult4Button.show()

			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult5.show()
			self.priceResult5.show()
			self.deleteResult5Button.show()
			self.nro5.show()
			self.seeResult5Button.show()

			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult6.show()
			self.priceResult6.show()
			self.deleteResult6Button.show()
			self.nro6.show()
			self.seeResult6Button.show()

			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult7.show()
			self.priceResult7.show()
			self.deleteResult7Button.show()
			self.nro7.show()
			self.seeResult7Button.show()

			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult8.show()
			self.priceResult8.show()
			self.deleteResult8Button.show()
			self.nro8.show()
			self.seeResult8Button.show()

			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult9.show()
			self.priceResult9.show()
			self.deleteResult9Button.show()
			self.nro9.show()
			self.seeResult9Button.show()

			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult10.show()
			self.priceResult10.show()
			self.deleteResult10Button.show()
			self.nro10.show()
			self.seeResult10Button.show()

			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])
			self.titleResult11.show()
			self.priceResult11.show()
			self.deleteResult11Button.show()
			self.nro11.show()
			self.seeResult11Button.show()

		if len(_line) == 36:
			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult1.show()
			self.priceResult1.show()
			self.deleteResult1Button.show()
			self.nro1.show()
			self.seeResult1Button.show()

			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult2.show()
			self.priceResult2.show()
			self.deleteResult2Button.show()
			self.nro2.show()
			self.seeResult2Button.show()

			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult3.show()
			self.priceResult3.show()
			self.deleteResult3Button.show()
			self.nro3.show()
			self.seeResult3Button.show()

			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult4.show()
			self.priceResult4.show()
			self.deleteResult4Button.show()
			self.nro4.show()
			self.seeResult4Button.show()

			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult5.show()
			self.priceResult5.show()
			self.deleteResult5Button.show()
			self.nro5.show()
			self.seeResult5Button.show()

			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult6.show()
			self.priceResult6.show()
			self.deleteResult6Button.show()
			self.nro6.show()
			self.seeResult6Button.show()

			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult7.show()
			self.priceResult7.show()
			self.deleteResult7Button.show()
			self.nro7.show()
			self.seeResult7Button.show()

			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult8.show()
			self.priceResult8.show()
			self.deleteResult8Button.show()
			self.nro8.show()
			self.seeResult8Button.show()

			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult9.show()
			self.priceResult9.show()
			self.deleteResult9Button.show()
			self.nro9.show()
			self.seeResult9Button.show()

			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult10.show()
			self.priceResult10.show()
			self.deleteResult10Button.show()
			self.nro10.show()
			self.seeResult10Button.show()

			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])
			self.titleResult11.show()
			self.priceResult11.show()
			self.deleteResult11Button.show()
			self.nro11.show()
			self.seeResult11Button.show()

			self.titleResult12.setText(_line[33])
			self.priceResult12.setText(_line[34])
			self.titleResult12.show()
			self.priceResult12.show()
			self.deleteResult12Button.show()
			self.nro12.show()
			self.seeResult12Button.show()

		self.closeSearchResultButton.show()
		self.openSearchResultButton.hide()

		self.closeProductsToPublishButton.hide()
		self.openProductsToPublishButton.show()

		self.productsPublishScreen.hide()
		self.searchResultScreen.show()

		self.settingsFrame.hide()
		self.closeSettingsButton.hide()
		self.openSettingsButton.show()

		self.addProductsButton.show()
		self.textAddedProducts.hide()

	def closeResultScreen(self):
		self.closeSearchResultButton.hide()
		self.openSearchResultButton.show()
		self.searchResultScreen.hide()

	def addProductsToPublish(self):

		self.textFullCapacity.hide()

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		g = open ('publish.txt')
		readPublish = g.read().splitlines()
		g.close()

		if len(readPublish) == 0:
			addToPublish = []
			g = open ('publish.txt','w+')

			for i in _line:
				addToPublish.append(i)

			for h in addToPublish:
				g.writelines(str(h) + "\n")
			
			g.close()

			self.textAddedProducts.show()
			# self.addedProducts.show()
			self.showProductsButton.show()
			
	
		else: 
			
			if len(readPublish) >= 36:
				self.textFullCapacity.show()
				self.textAddedProducts.hide()
				self.showProductsButton.show()
				

			else:

				quantityProducts = int((36 - len(readPublish))/3)
				quantityProductsOperation = int((len(_line))/3) - readPublish
				if quantityProductsOperation > 0:
					if quantityProducts == 1:
						
						self.textFullCapacity.setText("There is only room to add " + str(cantidadproducts) + " products.")
						self.textFullCapacity.show()
					else:
						
						self.textFullCapacity.setText("There is only room to add " + str(quantityProducts) + " products.")
						self.textFullCapacity.show()
				else:				

					g = open ('publish.txt','w+')

					addToPublish = []

					for t in readPublish:
						addToPublish.append(t)

					for i in _line:
						addToPublish.append(i)

					for h in addToPublish:
						g.writelines(str(h) + "\n")

					g.close()

					self.textFullCapacity.hide()
					self.textAddedProducts.show()
					self.showProductsButton.show()
					self.addProductsButton.hide()

		g.close()

	def closeProductsToPublishScreen(self):
		self.closeProductsToPublishButton.hide()
		self.openProductsToPublishButton.show()
		self.productsPublishScreen.hide()

	def showProductsToPublishScreen(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		self.publish1.hide()
		self.publish2.hide()
		self.publish3.hide()
		self.publish4.hide()
		self.publish5.hide()
		self.publish6.hide()
		self.publish7.hide()
		self.publish8.hide()
		self.publish9.hide()
		self.publish10.hide()
		self.publish11.hide()
		self.publish12.hide()

		if len(_line) == 3:
			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])

			self.publish1.show()

		if len(_line) == 6:
			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])

			self.publish1.hide()
			self.publish2.hide()

		if len(_line) == 9:
			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])

			self.publish1.hide()
			self.publish2.hide()
			self.publish3.hide()
		
		if len(_line) == 12:
			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])

			self.publish1.hide()
			self.publish2.hide()
			self.publish3.hide()
			self.publish4.hide()

		if len(_line) == 15:
			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])

			self.publish1.hide()
			self.publish2.hide()
			self.publish3.hide()
			self.publish4.hide()
			self.publish5.hide()

		if len(_line) == 18:
			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])

			self.publish1.hide()
			self.publish2.hide()
			self.publish3.hide()
			self.publish4.hide()
			self.publish5.hide()
			self.publish6.hide()


		if len(_line) == 21:
			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])

			self.publish1.hide()
			self.publish2.hide()
			self.publish3.hide()
			self.publish4.hide()
			self.publish5.hide()
			self.publish6.hide()
			self.publish7.hide()

		if len(_line) == 24:
			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])

			self.publish1.hide()
			self.publish2.hide()
			self.publish3.hide()
			self.publish4.hide()
			self.publish5.hide()
			self.publish6.hide()
			self.publish7.hide()
			self.publish8.hide()

		if len(_line) == 27:
			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])

			self.publish1.hide()
			self.publish2.hide()
			self.publish3.hide()
			self.publish4.hide()
			self.publish5.hide()
			self.publish6.hide()
			self.publish7.hide()
			self.publish8.hide()
			self.publish9.hide()


		if len(_line) == 30:
			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])

			self.publish1.hide()
			self.publish2.hide()
			self.publish3.hide()
			self.publish4.hide()
			self.publish5.hide()
			self.publish6.hide()
			self.publish7.hide()
			self.publish8.hide()
			self.publish9.hide()
			self.publish10.hide()

		
		if len(_line) == 33:
			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish1.hide()
			self.publish2.hide()
			self.publish3.hide()
			self.publish4.hide()
			self.publish5.hide()
			self.publish6.hide()
			self.publish7.hide()
			self.publish8.hide()
			self.publish9.hide()
			self.publish10.hide()
			self.publish11.hide()
	

		if len(_line) == 36:
			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])
			self.titlePublish12.setText(_line[33])
			self.pricePublish12.setText(_line[34])

			self.publish1.hide()
			self.publish2.hide()
			self.publish3.hide()
			self.publish4.hide()
			self.publish5.hide()
			self.publish6.hide()
			self.publish7.hide()
			self.publish8.hide()
			self.publish9.hide()
			self.publish10.hide()
			self.publish11.hide()
			self.publish12.hide()


		self.closeProductsToPublishButton.show()
		self.openProductsToPublishButton.hide()

		self.closeSearchResultButton.hide()
		self.openSearchResultButton.show()

		self.productsPublishScreen.show()

		self.searchResultScreen.hide()

		self.settingsFrame.hide()
		self.closeSettingsButton.hide()
		self.openSettingsButton.show()

	# Remove products displayed in Search Result Screen

	def deleteResult1(self):

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 0
		newItem = []

		if len(_line) == 36:

			for line in range(33):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])

			self.result12.hide()

		if len(_line) == 33:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(30):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])

			
			self.result11.hide()

		if len(_line) == 30:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(27):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			

			self.result10.hide()
			

		if len(_line) == 27:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(24):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			

			self.result9.hide()
			

		if len(_line) == 24:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(21):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			
			self.result8.hide()

		if len(_line) == 21:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(18):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])

			self.result7.hide()

		if len(_line) == 18:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])

			self.result6.hide()
			

		if len(_line) == 15:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])

			self.result5.hide()

		if len(_line) == 12:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			

			self.result4.hide()


		if len(_line) == 9:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])

			self.result3.hide()


		if len(_line) == 6:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			
			self.result2.hide()

		if len(_line) == 3:

			f = open ('links.txt','w+')
			f.writelines("")
			f.close()

			self.result1.hide()
			
			self.searchResultScreen.hide()

	def deleteResult2(self):

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 3
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])

		if len(_line) == 36:

			for line in range(30):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])

			self.result12.hide()

		if len(_line) == 33:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(27):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			
			self.result11.hide()

		if len(_line) == 30:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(24):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])

			self.result10.hide()


		if len(_line) == 27:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(21):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
		
			self.result9.hide()

		if len(_line) == 24:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(18):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])

			self.result8.hide()

		if len(_line) == 21:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])

			self.result7.hide()

		if len(_line) == 18:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])

			self.result6.hide()

		if len(_line) == 15:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])

			self.result5.hide()


		if len(_line) == 12:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])

			self.result4.hide()


		if len(_line) == 9:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
		

			self.result3.hide()


		if len(_line) == 6:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			
		

			self.result2.hide()

	def deleteResult3(self):

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 6
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])

		if len(_line) == 36:

			for line in range(27):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])

			self.result12.hide()

		if len(_line) == 33:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(24):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])

			self.result11.hide()

		if len(_line) == 30:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(21):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
		

			self.result10.hide()

		if len(_line) == 27:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(18):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])

			self.result9.hide()

		if len(_line) == 24:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])

			self.result8.hide()

		if len(_line) == 21:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])

			self.result7.hide()

		if len(_line) == 18:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])

			self.result6.hide()

		if len(_line) == 15:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])

			self.result5.hide()

		if len(_line) == 12:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])

			self.result4.hide()


		if len(_line) == 9:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])

			self.result3.hide()

	def deleteResult4(self):

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 9
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])

		if len(_line) == 36:

			for line in range(24):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])

			self.result12.hide()

		if len(_line) == 33:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(21):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])

			self.result11.hide()

		if len(_line) == 30:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(18):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])

			self.result10.hide()

		if len(_line) == 27:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])

			self.result9.hide()

		if len(_line) == 24:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])

			self.result8.hide()

		if len(_line) == 21:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])

			self.result7.hide()

		if len(_line) == 18:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])

			self.result6.hide()

		if len(_line) == 15:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])

			self.result5.hide()

		if len(_line) == 12:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])

			self.result4.hide()

	def deleteResult5(self):

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 12
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])

		if len(_line) == 36:

			for line in range(21):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])

			self.result12.hide()

		if len(_line) == 33:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 12
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			for line in range(18):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])

			self.result11.hide()

		if len(_line) == 30:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 12
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])

			self.result10.hide()

		if len(_line) == 27:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 12
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])

			self.result9.hide()

		if len(_line) == 24:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 12
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])

			self.result8.hide()

		if len(_line) == 21:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 12
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])

			self.result7.hide()

		if len(_line) == 18:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 12
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])

			self.result6.hide()

		if len(_line) == 15:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])

			self.result5.hide()

	def deleteResult6(self):

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 15
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])

		if len(_line) == 36:

			for line in range(18):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])

			self.result12.hide()

		if len(_line) == 33:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 15
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])

			self.result11.hide()

		if len(_line) == 30:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 15
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])

			self.result10.hide()

		if len(_line) == 27:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 15
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])

			self.result9.hide()

		if len(_line) == 24:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 15
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])

			self.result8.hide()

		if len(_line) == 21:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 15
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])

			self.result7.hide()

		if len(_line) == 18:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])

			self.result6.hide()

	def deleteResult7(self):

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 18
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])
		newItem.append(_line[15])
		newItem.append(_line[16])
		newItem.append(_line[17])

		if len(_line) == 36:

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])

			self.result12.hide()

		if len(_line) == 33:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 18
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])

			self.result11.hide()

		if len(_line) == 30:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 18
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])

			self.result10.hide()

		if len(_line) == 27:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 18
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])

			self.result9.hide()

		if len(_line) == 24:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 18
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])

			self.result8.hide()

		if len(_line) == 21:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])


			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])

			self.result7.hide()

	def deleteResult8(self):

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 21
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])
		newItem.append(_line[15])
		newItem.append(_line[16])
		newItem.append(_line[17])
		newItem.append(_line[18])
		newItem.append(_line[19])
		newItem.append(_line[20])

		if len(_line) == 36:

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])

			self.result12.hide()

		if len(_line) == 33:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 21
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])

			self.result11.hide()

		if len(_line) == 30:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 21
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])

			self.result10.hide()

		if len(_line) == 27:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 21
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])

			self.result9.hide()

		if len(_line) == 24:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])

			self.result8.hide()

	def deleteResult9(self):

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 24
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])
		newItem.append(_line[15])
		newItem.append(_line[16])
		newItem.append(_line[17])
		newItem.append(_line[18])
		newItem.append(_line[19])
		newItem.append(_line[20])
		newItem.append(_line[21])
		newItem.append(_line[22])
		newItem.append(_line[23])

		if len(_line) == 36:

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])

			self.result12.hide()

		if len(_line) == 33:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 24
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])
			newItem.append(_line[21])
			newItem.append(_line[22])
			newItem.append(_line[23])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])

			self.result11.hide()

		if len(_line) == 30:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 24
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])
			newItem.append(_line[21])
			newItem.append(_line[22])
			newItem.append(_line[23])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])

			self.result10.hide()

		if len(_line) == 27:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
		
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])
			newItem.append(_line[21])
			newItem.append(_line[22])
			newItem.append(_line[23])

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])

			self.result9.hide()

	def deleteResult10(self):

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 27
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])
		newItem.append(_line[15])
		newItem.append(_line[16])
		newItem.append(_line[17])
		newItem.append(_line[18])
		newItem.append(_line[19])
		newItem.append(_line[20])
		newItem.append(_line[21])
		newItem.append(_line[22])
		newItem.append(_line[23])
		newItem.append(_line[24])
		newItem.append(_line[25])
		newItem.append(_line[26])

		if len(_line) == 36:

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])

			self.result12.hide()

		if len(_line) == 33:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 27
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])
			newItem.append(_line[21])
			newItem.append(_line[22])
			newItem.append(_line[23])
			newItem.append(_line[24])
			newItem.append(_line[25])
			newItem.append(_line[26])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])

			self.result11.hide()

		if len(_line) == 30:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])
			newItem.append(_line[21])
			newItem.append(_line[22])
			newItem.append(_line[23])
			newItem.append(_line[24])
			newItem.append(_line[25])
			newItem.append(_line[26])

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])

			self.result10.hide()

	def deleteResult11(self):

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 30
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])
		newItem.append(_line[15])
		newItem.append(_line[16])
		newItem.append(_line[17])
		newItem.append(_line[18])
		newItem.append(_line[19])
		newItem.append(_line[20])
		newItem.append(_line[21])
		newItem.append(_line[22])
		newItem.append(_line[23])
		newItem.append(_line[24])
		newItem.append(_line[25])
		newItem.append(_line[26])
		newItem.append(_line[27])
		newItem.append(_line[28])
		newItem.append(_line[29])

		if len(_line) == 36:

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])

			self.result12.hide()


		if len(_line) == 33:

			f = open ('links.txt')
			_line = f.read().splitlines()
			f.close()
			
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])
			newItem.append(_line[21])
			newItem.append(_line[22])
			newItem.append(_line[23])
			newItem.append(_line[24])
			newItem.append(_line[25])
			newItem.append(_line[26])
			newItem.append(_line[27])
			newItem.append(_line[28])
			newItem.append(_line[29])

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])

			self.result11.hide()

	def deleteResult12(self):

		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 33
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])
		newItem.append(_line[15])
		newItem.append(_line[16])
		newItem.append(_line[17])
		newItem.append(_line[18])
		newItem.append(_line[19])
		newItem.append(_line[20])
		newItem.append(_line[21])
		newItem.append(_line[22])
		newItem.append(_line[23])
		newItem.append(_line[24])
		newItem.append(_line[25])
		newItem.append(_line[26])
		newItem.append(_line[27])
		newItem.append(_line[28])
		newItem.append(_line[29])
		newItem.append(_line[30])
		newItem.append(_line[31])
		newItem.append(_line[32])

		if len(_line) == 36:

			f = open ('links.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titleResult1.setText(_line[0])
			self.priceResult1.setText(_line[1])
			self.titleResult2.setText(_line[3])
			self.priceResult2.setText(_line[4])
			self.titleResult3.setText(_line[6])
			self.priceResult3.setText(_line[7])
			self.titleResult4.setText(_line[9])
			self.priceResult4.setText(_line[10])
			self.titleResult5.setText(_line[12])
			self.priceResult5.setText(_line[13])
			self.titleResult6.setText(_line[15])
			self.priceResult6.setText(_line[16])
			self.titleResult7.setText(_line[18])
			self.priceResult7.setText(_line[19])
			self.titleResult8.setText(_line[21])
			self.priceResult8.setText(_line[22])
			self.titleResult9.setText(_line[24])
			self.priceResult9.setText(_line[25])
			self.titleResult10.setText(_line[27])
			self.priceResult10.setText(_line[28])
			self.titleResult11.setText(_line[30])
			self.priceResult11.setText(_line[31])

			self.result12.hide()


	# Remove products added to the Products To Publish Screen

	def deleteProduct1(self):

		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 0
		newItem = []

		if len(_line) == 36:

			for line in range(33):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish12.hide()
		

		if len(_line) == 33:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(30):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])

			self.publish11.hide()

		if len(_line) == 30:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(27):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])

			self.publish10.hide()

		if len(_line) == 27:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(24):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])

			self.publish9.hide()

		if len(_line) == 24:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(21):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])

			self.publish8.hide()

		if len(_line) == 21:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(18):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])

			self.publish7.hide()

		if len(_line) == 18:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])

			self.publish6.hide()

		if len(_line) == 15:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])

			self.publish5.hide()

		if len(_line) == 12:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])

			self.publish4.hide()


		if len(_line) == 9:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])

			self.publish3.hide()


		if len(_line) == 6:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 0
			newItem = []

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])

			self.publish2.hide()

		if len(_line) == 3:

			f = open ('publish.txt','w+')
			f.writelines("")
			f.close()

			self.publish1.hide()
			self.productsPublishScreen.hide()

	def deleteProduct2(self):

		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 3
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])

		if len(_line) == 36:

			for line in range(30):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish12.hide()

		if len(_line) == 33:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(27):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])

			self.publish11.hide()

		if len(_line) == 30:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(24):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])

			self.publish10.hide()

		if len(_line) == 27:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(21):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])

			self.publish9.hide()

		if len(_line) == 24:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(18):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])

			self.publish8.hide()

		if len(_line) == 21:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])

			self.publish7.hide()

		if len(_line) == 18:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])

			self.publish6.hide()

		if len(_line) == 15:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])

			self.publish5.hide()

		if len(_line) == 12:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])

			self.publish4.hide()


		if len(_line) == 9:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])

			self.publish3.hide()


		if len(_line) == 6:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 3
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])

			self.publish2.hide()

	def deleteProduct3(self):

		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 6
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])

		if len(_line) == 36:

			for line in range(27):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish12.hide()

		if len(_line) == 33:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(24):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])

			self.publish11.hide()

		if len(_line) == 30:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(21):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])

			self.publish10.hide()

		if len(_line) == 27:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(18):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])

			self.publish9.hide()

		if len(_line) == 24:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])

			self.publish8.hide()

		if len(_line) == 21:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])

			self.publish7.hide()

		if len(_line) == 18:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])

			self.publish6.hide()

		if len(_line) == 15:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])

			self.publish5.hide()

		if len(_line) == 12:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 6
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])

			self.publish4.hide()

		if len(_line) == 9:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])

			self.publish3.hide()

	def deleteProduct4(self):

		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 9
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])

		if len(_line) == 36:

			for line in range(24):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish12.hide()

		if len(_line) == 33:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(21):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titulo1Publicar.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titulo1Publicar.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titulo1Publicar.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titulo1Publicar.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titulo1Publicar.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titulo1Publicar.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titulo1Publicar.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titulo1Publicar.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titulo1Publicar.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titulo1Publicar0.setText(_line[27])
			self.pricePublish10.setText(_line[28])

			self.publish11.hide()

		if len(_line) == 30:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(18):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])

			self.publish10.hide()

		if len(_line) == 27:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])

			self.publish9.hide()

		if len(_line) == 24:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])

			self.publish8.hide()

		if len(_line) == 21:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])

			self.publish7.hide()

		if len(_line) == 18:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])

			self.publish6.hide()

		if len(_line) == 15:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 9
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])

			self.publish5.hide()

		if len(_line) == 12:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])

			self.publish4.hide()

	def deleteProduct5(self):

		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 12
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])

		if len(_line) == 36:

			for line in range(21):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish12.hide()

		if len(_line) == 33:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 12
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			for line in range(18):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])

			self.publish11.hide()

		if len(_line) == 30:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 12
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])

			self.publish10.hide()

		if len(_line) == 27:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 12
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])

			self.publish9.hide()

		if len(_line) == 24:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 12
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])

			self.publish8.hide()

		if len(_line) == 21:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 12
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])

			self.publish7.hide()

		if len(_line) == 18:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 12
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])

			self.publish6.hide()

		if len(_line) == 15:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])

			self.publish5.hide()

	def deleteProduct6(self):

		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 15
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])

		if len(_line) == 36:

			for line in range(18):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish12.hide()

		if len(_line) == 33:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 15
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])

			self.publish11.hide()

		if len(_line) == 30:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 15
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])

			self.publish10.hide()

		if len(_line) == 27:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 15
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])

			self.publish9.hide()

		if len(_line) == 24:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 15
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])

			self.publish8.hide()

		if len(_line) == 21:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 15
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])

			self.publish7.hide()

		if len(_line) == 18:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])

			self.publish6.hide()

	def deleteProduct7(self):

		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 18
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])
		newItem.append(_line[15])
		newItem.append(_line[16])
		newItem.append(_line[17])

		if len(_line) == 36:

			for line in range(15):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish12.hide()

		if len(_line) == 33:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 18
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])

			self.publish11.hide()

		if len(_line) == 30:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 18
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])

			self.publish10.hide()

		if len(_line) == 27:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 18
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])

			self.publish9.hide()

		if len(_line) == 24:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 18
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])

			self.publish8.hide()

		if len(_line) == 21:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])


			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])

			self.publish7.hide()

	def deleteProduct8(self):

		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 21
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])
		newItem.append(_line[15])
		newItem.append(_line[16])
		newItem.append(_line[17])
		newItem.append(_line[18])
		newItem.append(_line[19])
		newItem.append(_line[20])

		if len(_line) == 36:

			for line in range(12):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish12.hide()

		if len(_line) == 33:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 21
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])

			self.publish11.hide()


		if len(_line) == 30:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 21
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])

			self.publish10.hide()

		if len(_line) == 27:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 21
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])

			self.publish9.hide()

		if len(_line) == 24:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])

			self.publish8.hide()

	def deleteProduct9(self):

		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 24
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])
		newItem.append(_line[15])
		newItem.append(_line[16])
		newItem.append(_line[17])
		newItem.append(_line[18])
		newItem.append(_line[19])
		newItem.append(_line[20])
		newItem.append(_line[21])
		newItem.append(_line[22])
		newItem.append(_line[23])

		if len(_line) == 36:

			for line in range(9):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish12.hide()

		if len(_line) == 33:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 24
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])
			newItem.append(_line[21])
			newItem.append(_line[22])
			newItem.append(_line[23])

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])

			self.publish11.hide()

		if len(_line) == 30:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 24
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])
			newItem.append(_line[21])
			newItem.append(_line[22])
			newItem.append(_line[23])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])

			self.publish10.hide()

		if len(_line) == 27:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
		
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])
			newItem.append(_line[21])
			newItem.append(_line[22])
			newItem.append(_line[23])

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])

			self.publish9.hide()

	def deleteProduct10(self):

		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 27
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])
		newItem.append(_line[15])
		newItem.append(_line[16])
		newItem.append(_line[17])
		newItem.append(_line[18])
		newItem.append(_line[19])
		newItem.append(_line[20])
		newItem.append(_line[21])
		newItem.append(_line[22])
		newItem.append(_line[23])
		newItem.append(_line[24])
		newItem.append(_line[25])
		newItem.append(_line[26])

		if len(_line) == 36:

			for line in range(6):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish12.hide()

		if len(_line) == 33:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			countLine = 27
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])
			newItem.append(_line[21])
			newItem.append(_line[22])
			newItem.append(_line[23])
			newItem.append(_line[24])
			newItem.append(_line[25])
			newItem.append(_line[26])

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])

			self.publish11.hide()

		if len(_line) == 30:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])
			newItem.append(_line[21])
			newItem.append(_line[22])
			newItem.append(_line[23])
			newItem.append(_line[24])
			newItem.append(_line[25])
			newItem.append(_line[26])

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])

			self.publish10.hide()

	def deleteProduct11(self):

		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 30
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])
		newItem.append(_line[15])
		newItem.append(_line[16])
		newItem.append(_line[17])
		newItem.append(_line[18])
		newItem.append(_line[19])
		newItem.append(_line[20])
		newItem.append(_line[21])
		newItem.append(_line[22])
		newItem.append(_line[23])
		newItem.append(_line[24])
		newItem.append(_line[25])
		newItem.append(_line[26])
		newItem.append(_line[27])
		newItem.append(_line[28])
		newItem.append(_line[29])

		if len(_line) == 36:

			for line in range(3):
				_line[countLine] = _line[countLine+3]
				newItem.append(_line[countLine])
				countLine += 1

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish12.hide()

		if len(_line) == 33:

			f = open ('publish.txt')
			_line = f.read().splitlines()
			f.close()
			
			newItem = []
			newItem.append(_line[0])
			newItem.append(_line[1])
			newItem.append(_line[2])
			newItem.append(_line[3])
			newItem.append(_line[4])
			newItem.append(_line[5])
			newItem.append(_line[6])
			newItem.append(_line[7])
			newItem.append(_line[8])
			newItem.append(_line[9])
			newItem.append(_line[10])
			newItem.append(_line[11])
			newItem.append(_line[12])
			newItem.append(_line[13])
			newItem.append(_line[14])
			newItem.append(_line[15])
			newItem.append(_line[16])
			newItem.append(_line[17])
			newItem.append(_line[18])
			newItem.append(_line[19])
			newItem.append(_line[20])
			newItem.append(_line[21])
			newItem.append(_line[22])
			newItem.append(_line[23])
			newItem.append(_line[24])
			newItem.append(_line[25])
			newItem.append(_line[26])
			newItem.append(_line[27])
			newItem.append(_line[28])
			newItem.append(_line[29])

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])

			self.publish11.hide()

	def deleteProduct12(self):

		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()
		countLine = 33
		newItem = []
		newItem.append(_line[0])
		newItem.append(_line[1])
		newItem.append(_line[2])
		newItem.append(_line[3])
		newItem.append(_line[4])
		newItem.append(_line[5])
		newItem.append(_line[6])
		newItem.append(_line[7])
		newItem.append(_line[8])
		newItem.append(_line[9])
		newItem.append(_line[10])
		newItem.append(_line[11])
		newItem.append(_line[12])
		newItem.append(_line[13])
		newItem.append(_line[14])
		newItem.append(_line[15])
		newItem.append(_line[16])
		newItem.append(_line[17])
		newItem.append(_line[18])
		newItem.append(_line[19])
		newItem.append(_line[20])
		newItem.append(_line[21])
		newItem.append(_line[22])
		newItem.append(_line[23])
		newItem.append(_line[24])
		newItem.append(_line[25])
		newItem.append(_line[26])
		newItem.append(_line[27])
		newItem.append(_line[28])
		newItem.append(_line[29])
		newItem.append(_line[30])
		newItem.append(_line[31])
		newItem.append(_line[32])

		if len(_line) == 36:

			f = open ('publish.txt','w+')
			for t in newItem:
				f.writelines(str(t) + "\n")
			f.close()

			self.titlePublish1.setText(_line[0])
			self.pricePublish1.setText(_line[1])
			self.titlePublish2.setText(_line[3])
			self.pricePublish2.setText(_line[4])
			self.titlePublish3.setText(_line[6])
			self.pricePublish3.setText(_line[7])
			self.titlePublish4.setText(_line[9])
			self.pricePublish4.setText(_line[10])
			self.titlePublish5.setText(_line[12])
			self.pricePublish5.setText(_line[13])
			self.titlePublish6.setText(_line[15])
			self.pricePublish6.setText(_line[16])
			self.titlePublish7.setText(_line[18])
			self.pricePublish7.setText(_line[19])
			self.titlePublish8.setText(_line[21])
			self.pricePublish8.setText(_line[22])
			self.titlePublish9.setText(_line[24])
			self.pricePublish9.setText(_line[25])
			self.titlePublish10.setText(_line[27])
			self.pricePublish10.setText(_line[28])
			self.titlePublish11.setText(_line[30])
			self.pricePublish11.setText(_line[31])

			self.publish12.hide()

	# Functions for the "view product" button in "Search Result Screen".

	def seeProductsResult1(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[2])

	def seeProductsResult2(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[5])

	def seeProductsResult3(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[8])

	def seeProductsResult4(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[11])

	def seeProductsResult5(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[14])

	def seeProductsResult6(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[17])

	def seeProductsResult7(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[20])

	def seeProductsResult8(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[23])

	def seeProductsResult9(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[26])

	def seeProductsResult10(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[29])

	def seeProductsResult11(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[32])

	def seeProductsResult12(self):
		f = open ('links.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[35])

	# Functions for the "view product" button in the "Publish Products Screen".

	def seeProductsPublish1(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[2])

	def seeProductsPublish2(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[5])

	def seeProductsPublish3(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[8])

	def seeProductsPublish4(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[11])

	def seeProductsPublish5(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[14])

	def seeProductsPublish6(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[17])

	def seeProductsPublish7(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[20])

	def seeProductsPublish8(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[23])

	def seeProductsPublish9(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[26])

	def seeProductsPublish10(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[29])

	def seeProductsPublish11(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[32])

	def seeProductsPublish12(self):
		f = open ('publish.txt')
		_line = f.read().splitlines()
		f.close()

		webbrowser.open(_line[35])

	def publishProducts(self):
		self.timePublish.hide()
		self.textTelegramMinutes.hide()
		self.textPublishEvery.hide()
		self.deleteProduct1Button.hide()
		self.deleteProduct2Button.hide()
		self.deleteProduct3Button.hide()
		self.deleteProduct4Button.hide()
		self.deleteProduct5Button.hide()
		self.deleteProduct6Button.hide()
		self.deleteProduct7Button.hide()
		self.deleteProduct8Button.hide()
		self.deleteProduct9Button.hide()
		self.deleteProduct10Button.hide()
		self.deleteProduct11Button.hide()
		self.deleteProduct12Button.hide()

		if self.timePublish.text() == "":
			self.timePublish.setText("0")

		self.thread[1] = ThreadPublish(parent=None, index=1, timeToPublish = self.timePublish.text())
		if self.thread[1].start():
			self.thread[1].stop()
		else:
			self.thread[1].start()
			self.thread[1].any_signal.connect(self.productsToPublish)

	def productsToPublish(self, counter):

		ctn = counter

		self.timeToPublish = self.timePublish.text()

		self.stopPublishButton.show()
		self.publishButton.hide()

		self.textPublishedQuantity.setText("Publishing products...")
		self.textPublishedQuantity.show()	


		if ctn >= 1:
			self.textPublishedQuantity.setText(str(ctn) + " of 12 published products.")

		if ctn == 12:
			self.textPublishedQuantity.hide()
			QMessageBox.information(self, '¡Ready!', 'All products have been published.')
			self.stopPublishButton.hide()
			self.publishButton.show()

			self.timePublish.show()
			self.textTelegramMinutes.show()
			self.textPublishEvery.show()


		if ctn == 14:
			QMessageBox.information(self, '¡Error!', 'An error has occurred, please try again or contact the developer.')	
			self.stopPublishButton.hide()
			self.publishButton.show()
			self.timePublish.show()
			self.textTelegramMinutes.show()
			self.textPublishEvery.show()			

	def searchProduct(self):
		self.searchResultScreen.hide()
		self.productsPublishScreen.hide()
			
		if self.amazonES.isChecked():
			self.thread[1] = amazones(parent=None, index=1, keyword = self.formSearch.text())
			if self.thread[1].start():
				self.thread[1].stop()
			else:
				self.thread[1].start()
				self.thread[1].any_signal.connect(self.indexFunction)

		elif self.amazonUS.isChecked():
			self.thread[1] = amazonus(parent=None, index=1, keyword = self.formSearch.text())
			if self.thread[1].start():
				self.thread[1].stop()
			else:
				self.thread[1].start()
				self.thread[1].any_signal.connect(self.indexFunction)

		elif self.amazonIT.isChecked():
			self.thread[1] = amazonit(parent=None, index=1, keyword = self.formSearch.text())
			if self.thread[1].start():
				self.thread[1].stop()
			else:
				self.thread[1].start()
				self.thread[1].any_signal.connect(self.indexFunction)
		
		else:
			QMessageBox.information(self, 'Error', 'You must select an Amazon region.')

	def indexFunction(self, counter):

		ctn = counter

		index = self.sender().index
		if index == 1:
			if ctn == 1:

				keyword = self.formSearch.text()

				if len(keyword) == 0:
					self.thread[1].stop()
					QMessageBox.information(self, 'Error', 'You must place the name of the product or a direct link to the product.')
					

				else:
					
					self.searchBarFrame.show()
					self.searchFrame.hide()
					self.searchProgress.setValue(ctn)
			else:
				self.searchProgress.setValue(ctn)

		if ctn == 5:
			self.textProgress.setText("Configuring Google Chrome...")

		if ctn == 14:
			QMessageBox.information(self, 'Error', 'An unexpected error has occurred, please try again.')
			self.stopProcess()

		if ctn == 15:
			self.textProgress.setText("Connecting to Amazon...")

		if ctn == 25:
			self.textProgress.setText("Searching for products...")

		if ctn == 29:
			self.textProgress.setText("Adding products...")

		if ctn == 39:
			QMessageBox.information(self, 'Error', 'You must first configure in Settings your AmazonID, Telegram Token and ChatID.')
			self.stopProcess()

		if ctn == 100:
			self.searchBarFrame.hide()
			self.searchFrame.show()
			self.showResultsScreen()
			self.thread[1].stop()
			
class amazones(QtCore.QThread):
	any_signal = QtCore.pyqtSignal(int)

	def __init__(self, parent=None, index=0, keyword = ""):
		super(amazones, self).__init__(parent)
		self.index=index
		self.keyword = keyword
		self.is_running = True
	

	def run(self):
		print('Starting thread...', self.index)
		print(self.keyword)

		ctn=1
		self.any_signal.emit(ctn)

		if self.keyword.startswith("http"):

			try:

				f = open ('config.txt')
				readLines = f.read().splitlines()
				f.close()

				if len(readLines) == 0:
					self.any_signal.emit(39)
				else:
					f = open ('config.txt', 'r')
					idclient_line     = lc.getline('config.txt', 1).rstrip('\n')
					apitelegram_line  = lc.getline('config.txt', 2).rstrip('\n')
					chatid_line       = lc.getline('config.txt', 3).rstrip('\n')
					f.close()
				

				self.any_signal.emit(5)

				
				headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 'referer':'https://google.es',}
				
				url = self.keyword

				req = requests.get(url, headers=headers, timeout=10)

				soup = BeautifulSoup(req.text, "html.parser")
				
				self.any_signal.emit(25)
											
				product_title = soup.find('span',  id="productTitle").text.strip()
				
				try:
					product_price = soup.find_all('span', class_="a-size-base a-color-price")
					if len(product_price) == 0 or len(product_price) >= 2:
						product_price = soup.find_all('span', id="color_name_0_price")
						if len(product_price) == 0 or len(product_price) >= 2:
							product_price = soup.find('span', class_="a-offscreen").text.strip()
						else:
							product_price = soup.find('span', id="color_name_0_price").text.strip()[13:]
					else:
						product_price = soup.find('span', class_="a-size-base a-color-price").text.strip()
							
				except:
					product_price = "0"
							
				print(product_price)
				product_price = product_price.replace(',' , '.')
					
				if product_price.startswith("US$"):
					product_price = product_price.replace('US$' , '')
				else:
					product_price = product_price.replace('€' , '')

				product_price = product_price.replace('\n' , '.')
				product_count = product_price.count('.')
				if product_count <= 1:
					product_price = float(product_price)
				else:
					product_price = product_price.replace('.' , '', 1)
					product_price = float(product_price)

				product_link   = self.keyword + "&tag=" + idclient_line
				sleep(15)
				link_short = Shortener().tinyurl.short(product_link)

				f = open ('links.txt','w+')
				_line = f.read().splitlines()

				self.any_signal.emit(29)

				addToResult = [product_title, product_price, link_short]

				for i in _line:
					addToResult.append(i)

				for h in addToResult:
					f.writelines(str(h) + "\n")

				f.close()

				self.any_signal.emit(100)
		
			except:
				self.any_signal.emit(14)
				
		else:

			while ctn == 1:

				f = open ('config.txt')
				readLines = f.read().splitlines()
				f.close()

				if len(readLines) == 0:
					self.any_signal.emit(39)
				else:
					f = open ('config.txt', 'r')
					idclient_line     = lc.getline('config.txt', 1).rstrip('\n')
					apitelegram_line  = lc.getline('config.txt', 2).rstrip('\n')
					chatid_line       = lc.getline('config.txt', 3).rstrip('\n')
					f.close()
				
				ctn = 5
				self.any_signal.emit(ctn)
					

				try:
					
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 'referer':'https://google.es',}

					ctn = 15
					self.any_signal.emit(ctn)

					url = 'https://www.amazon.es/s?k=' + self.keyword

					req = requests.get(url, headers=headers, timeout=10)

					soup = BeautifulSoup(req.text, "html.parser")

					products_list = soup.find_all('div', class_="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20")

					total_item = []

					px = 0
					ct = 0
					ctn = 25
					self.any_signal.emit(25)

					for product in products_list:
						if px <= 21:
							print("--------------------------------------------------------------")

							product_title = product.find_all('span', class_="a-size-base-plus a-color-base a-text-normal")
							print(product_title)

							if len(product_title) <= 0:
								product_title  = product.find_all('span', class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")
							
								if len(product_title) <= 0:
									product_title = product.find('span', class_="a-size-base-plus a-color-base a-text-normal").text.strip()
								else:
									product_title = product.find('span', class_="a-size-base-plus a-color-base a-text-normal").text.strip()
							else:
								product_title = product.find('span', class_="a-size-base-plus a-color-base a-text-normal").text.strip()

							print(product_title)

							product_price = product.find('span', class_="a-price-whole")
							if product_price is None:
								product_price = 0
								px = px - 2
						
							else:
								
								product_price = product.find('span', class_="a-price-whole").text.strip()
								
								product_price = product_price.replace('.' , '')
								product_price = product_price.replace(',' , '.')
								product_price = float(product_price)
								product_link   = 'https://amazon.es'+product.find('a', class_='a-link-normal s-no-outline').get('href')+'&tag='+ idclient_line
							

		
								try:	
									link_short = Shortener().tinyurl.short(product_link)
									add_item = str(product_title) + "\n" + str(product_price) + "\n" + str(link_short)
								except:
									sleep(20)
									link_short = Shortener().tinyurl.short(product_link)
									add_item = str(product_title) + "\n" + str(product_price) + "\n" + str(link_short)

								total_item.append(add_item)

								
								ctn = ctn + 4
								self.any_signal.emit(ctn)

								ct = ct + 1 # Contará la cantidad de products encontrados


								if ct == 12:
									break
							print(product_price)
						else:
							break
						px = px + 1

					f = open ('links.txt','w+')
					for t in total_item:
						f.writelines(str(t) + "\n")
					f.close()	

					self.any_signal.emit(100)

				except:
					self.any_signal.emit(14)

				ctn = 2

	def stop(self):
		self.is_running = False
		print('Stopping thread...', self.index)
		self.terminate()

class amazonus(QtCore.QThread):
	any_signal = QtCore.pyqtSignal(int)

	def __init__(self, parent=None, index=0, keyword = ""):
		super(amazonus, self).__init__(parent)
		self.index=index
		self.keyword = keyword
		self.is_running = True
	

	def run(self):
		print('Starting thread...', self.index)
		print(self.keyword)

		ctn=1
		self.any_signal.emit(ctn)

		if self.keyword.startswith("http"):

			try:

				f = open ('config.txt')
				readLines = f.read().splitlines()
				f.close()

				if len(readLines) == 0:
					self.any_signal.emit(39)
				else:
					f = open ('config.txt', 'r')
					idclient_line     = lc.getline('config.txt', 1).rstrip('\n')
					apitelegram_line  = lc.getline('config.txt', 2).rstrip('\n')
					chatid_line       = lc.getline('config.txt', 3).rstrip('\n')
					f.close()
				

				self.any_signal.emit(5)

				
				headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 'referer':'https://google.es',}
				
				url = self.keyword

				req = requests.get(url, headers=headers, timeout=10)

				soup = BeautifulSoup(req.text, "html.parser")
				
				self.any_signal.emit(25)
											
				product_title = soup.find('span',  id="productTitle").text.strip()
				
				try:
					product_price = soup.find_all('span', class_="a-size-base a-color-price")
					if len(product_price) == 0 or len(product_price) >= 2:
						product_price = soup.find_all('span', id="color_name_0_price")
						if len(product_price) == 0 or len(product_price) >= 2:
							product_price = soup.find('span', class_="a-offscreen").text.strip()
						else:
							product_price = soup.find('span', id="color_name_0_price").text.strip()[13:]
					else:
						product_price = soup.find('span', class_="a-size-base a-color-price").text.strip()
							
				except:
					product_price = "0"
							
				print(product_price)
				product_price = product_price.replace(',' , '.')
					
				if product_price.startswith("US$"):
					product_price = product_price.replace('US$' , '')
				else:
					product_price = product_price.replace('€' , '')

				product_price = product_price.replace('\n' , '.')
				product_count = product_price.count('.')
				if product_count <= 1:
					product_price = float(product_price)
				else:
					product_price = product_price.replace('.' , '', 1)
					product_price = float(product_price)

				product_link   = self.keyword + "&tag=" + idclient_line
				sleep(15)
				link_short = Shortener().tinyurl.short(product_link)

				f = open ('links.txt','w+')
				_line = f.read().splitlines()

				self.any_signal.emit(29)

				addToResult = [product_title, product_price, link_short]

				for i in _line:
					addToResult.append(i)

				for h in addToResult:
					f.writelines(str(h) + "\n")

				f.close()

				self.any_signal.emit(100)
		
			except:
				self.any_signal.emit(14)
				

		else:

			while ctn == 1:

				f = open ('config.txt')
				readLines = f.read().splitlines()
				f.close()

				if len(readLines) == 0:
					self.any_signal.emit(39)
				else:
					f = open ('config.txt', 'r')
					idclient_line     = lc.getline('config.txt', 1).rstrip('\n')
					apitelegram_line  = lc.getline('config.txt', 2).rstrip('\n')
					chatid_line       = lc.getline('config.txt', 3).rstrip('\n')
					f.close()
				
				ctn = 5
				self.any_signal.emit(ctn)
					

				try:
					
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 'referer':'https://google.es',}

					ctn = 15
					self.any_signal.emit(ctn)

					url = 'https://www.amazon.us/s?k=' + self.keyword

					req = requests.get(url, headers=headers, timeout=10)

					soup = BeautifulSoup(req.text, "html.parser")

					products_list = soup.find_all('div', class_="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20")

					total_item = []

					px = 0
					ct = 0
					ctn = 25
					self.any_signal.emit(25)

					for product in products_list:
						if px <= 21:
							print("--------------------------------------------------------------")

							product_title = product.find_all('span', class_="a-size-base-plus a-color-base a-text-normal")
							print(product_title)

							if len(product_title) <= 0:
								product_title  = product.find_all('span', class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")
							
								if len(product_title) <= 0:
									product_title = product.find('span', class_="a-size-base-plus a-color-base a-text-normal").text.strip()
								else:
									product_title = product.find('span', class_="a-size-base-plus a-color-base a-text-normal").text.strip()
							else:
								product_title = product.find('span', class_="a-size-base-plus a-color-base a-text-normal").text.strip()

							print(product_title)

							product_price = product.find('span', class_="a-price-whole")
							if product_price is None:
								product_price = 0
								px = px - 2
						
							else:
								
								product_price = product.find('span', class_="a-price-whole").text.strip()
								
								product_price = product_price.replace('.' , '')
								product_price = product_price.replace(',' , '.')
								product_price = float(product_price)
								product_link   = 'https://amazon.us'+product.find('a', class_='a-link-normal s-no-outline').get('href')+'&tag='+ idclient_line
							

		
								try:	
									link_short = Shortener().tinyurl.short(product_link)
									add_item = str(product_title) + "\n" + str(product_price) + "\n" + str(link_short)
								except:
									sleep(20)
									link_short = Shortener().tinyurl.short(product_link)
									add_item = str(product_title) + "\n" + str(product_price) + "\n" + str(link_short)

								total_item.append(add_item)

								
								ctn = ctn + 4
								self.any_signal.emit(ctn)

								ct = ct + 1 # Contará la cantidad de products encontrados


								if ct == 12:
									break
							print(product_price)
						else:
							break
						px = px + 1


					f = open ('links.txt','w+')
					for t in total_item:
						f.writelines(str(t) + "\n")
					f.close()	

					self.any_signal.emit(100)

				except:
					self.any_signal.emit(14)

				ctn = 2

	def stop(self):
		self.is_running = False
		print('Stopping thread...', self.index)
		self.terminate()

class amazonit(QtCore.QThread):
	any_signal = QtCore.pyqtSignal(int)

	def __init__(self, parent=None, index=0, keyword = ""):
		super(amazonit, self).__init__(parent)
		self.index=index
		self.keyword = keyword
		self.is_running = True
	

	def run(self):
		print('Starting thread...', self.index)
		print(self.keyword)

		ctn=1
		self.any_signal.emit(ctn)

		if self.keyword.startswith("http"):

			try:

				f = open ('config.txt')
				readLines = f.read().splitlines()
				f.close()

				if len(readLines) == 0:
					self.any_signal.emit(39)
				else:
					f = open ('config.txt', 'r')
					idclient_line     = lc.getline('config.txt', 1).rstrip('\n')
					apitelegram_line  = lc.getline('config.txt', 2).rstrip('\n')
					chatid_line       = lc.getline('config.txt', 3).rstrip('\n')
					f.close()
				

				self.any_signal.emit(5)

				
				headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 'referer':'https://google.es',}
				
				url = self.keyword

				req = requests.get(url, headers=headers, timeout=10)

				soup = BeautifulSoup(req.text, "html.parser")
				
				self.any_signal.emit(25)
											
				product_title = soup.find('span',  id="productTitle").text.strip()
				
				try:
					product_price = soup.find_all('span', class_="a-size-base a-color-price")
					if len(product_price) == 0 or len(product_price) >= 2:
						product_price = soup.find_all('span', id="color_name_0_price")
						if len(product_price) == 0 or len(product_price) >= 2:
							product_price = soup.find('span', class_="a-offscreen").text.strip()
						else:
							product_price = soup.find('span', id="color_name_0_price").text.strip()[13:]
					else:
						product_price = soup.find('span', class_="a-size-base a-color-price").text.strip()
							
				except:
					product_price = "0"
							
				print(product_price)
				product_price = product_price.replace(',' , '.')
					
				if product_price.startswith("US$"):
					product_price = product_price.replace('US$' , '')
				else:
					product_price = product_price.replace('€' , '')

				product_price = product_price.replace('\n' , '.')
				product_count = product_price.count('.')
				if product_count <= 1:
					product_price = float(product_price)
				else:
					product_price = product_price.replace('.' , '', 1)
					product_price = float(product_price)

				product_link   = self.keyword + "&tag=" + idclient_line
				sleep(15)
				link_short = Shortener().tinyurl.short(product_link)

				f = open ('links.txt','w+')
				_line = f.read().splitlines()

				self.any_signal.emit(29)

				addToResult = [product_title, product_price, link_short]

				for i in _line:
					addToResult.append(i)

				for h in addToResult:
					f.writelines(str(h) + "\n")

				f.close()

				self.any_signal.emit(100)
		
			except:
				self.any_signal.emit(14)
				
		else:

			while ctn == 1:

				f = open ('config.txt')
				readLines = f.read().splitlines()
				f.close()

				if len(readLines) == 0:
					self.any_signal.emit(39)
				else:
					f = open ('config.txt', 'r')
					idclient_line     = lc.getline('config.txt', 1).rstrip('\n')
					apitelegram_line  = lc.getline('config.txt', 2).rstrip('\n')
					chatid_line       = lc.getline('config.txt', 3).rstrip('\n')
					f.close()
				
				ctn = 5
				self.any_signal.emit(ctn)
					

				try:
					
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 'referer':'https://google.es',}

					ctn = 15
					self.any_signal.emit(ctn)

					url = 'https://www.amazon.it/s?k=' + self.keyword

					req = requests.get(url, headers=headers, timeout=10)

					soup = BeautifulSoup(req.text, "html.parser")

					products_list = soup.find_all('div', class_="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20")

					total_item = []

					px = 0
					ct = 0
					ctn = 25
					self.any_signal.emit(25)

					for product in products_list:
						if px <= 21:
							print("--------------------------------------------------------------")

							product_title = product.find_all('span', class_="a-size-base-plus a-color-base a-text-normal")
							print(product_title)

							if len(product_title) <= 0:
								product_title  = product.find_all('span', class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")
							
								if len(product_title) <= 0:
									product_title = product.find('span', class_="a-size-base-plus a-color-base a-text-normal").text.strip()
								else:
									product_title = product.find('span', class_="a-size-base-plus a-color-base a-text-normal").text.strip()
							else:
								product_title = product.find('span', class_="a-size-base-plus a-color-base a-text-normal").text.strip()

							print(product_title)

							product_price = product.find('span', class_="a-price-whole")
							if product_price is None:
								product_price = 0
								px = px - 2
						
							else:
								
								product_price = product.find('span', class_="a-price-whole").text.strip()
								
								product_price = product_price.replace('.' , '')
								product_price = product_price.replace(',' , '.')
								product_price = float(product_price)
								product_link   = 'https://amazon.it'+product.find('a', class_='a-link-normal s-no-outline').get('href')+'&tag='+ idclient_line
							

		
								try:	
									link_short = Shortener().tinyurl.short(product_link)
									add_item = str(product_title) + "\n" + str(product_price) + "\n" + str(link_short)
								except:
									sleep(20)
									link_short = Shortener().tinyurl.short(product_link)
									add_item = str(product_title) + "\n" + str(product_price) + "\n" + str(link_short)

								total_item.append(add_item)

								
								ctn = ctn + 4
								self.any_signal.emit(ctn)

								ct = ct + 1 # Contará la cantidad de products encontrados


								if ct == 12:
									break
							print(product_price)
						else:
							break
						px = px + 1

					
					f = open ('links.txt','w+')
					for t in total_item:
						f.writelines(str(t) + "\n")
					f.close()	

					self.any_signal.emit(100)

				except Exception as e:
					self.any_signal.emit(14)
					
				ctn = 2

	def stop(self):
		self.is_running = False
		print('Stopping thread...', self.index)
		self.terminate()

class ThreadPublish(QtCore.QThread):
	any_signal = QtCore.pyqtSignal(int)

	def __init__(self, parent=None, index=0, timeToPublish=""):
		super(ThreadPublish, self).__init__(parent)
		self.index=index
		self.timeToPublish = timeToPublish
		self.is_running = True
	

	def run(self):
		try:
			self.any_signal.emit(0)

			f = open ('config.txt', 'r')
			idclient_line     = lc.getline('config.txt', 1).rstrip('\n')
			apitelegram_line  = lc.getline('config.txt', 2).rstrip('\n')
			chatid_line       = lc.getline('config.txt', 3).rstrip('\n')
			
			f.close()

			c_link  = 2 # To count the links
			c_titulo = 0 # To count the title
			c_precio = 1 # To count the price
			c_publicados = 0 # To count the number of published products

			f = open("publish.txt")
			read_text  = f.read().splitlines()
			f.close()

			for x in range(int(len(read_text)/3)):

				product_link = str(read_text[c_link])
				c_link = c_link + 3

				product_title = str(read_text[c_titulo])
				c_titulo = c_titulo + 3
				
				if len(product_title) == 0:
					break

				else:
					
					product_price = float(read_text[c_precio])
					c_precio = c_precio + 3
							
					sleep(float(self.timeToPublish)*60)

					requests.post('https://api.telegram.org/bot' + apitelegram_line + "/sendMessage",
					
					data = {'chat_id' : chatid_line, 
							'text': 

							'🚀 ' + product_title + '\n \n 🔥 Oferta : ' + str(product_price) + ' € \n ✘   Antes  : ' + str(round(product_price + (product_price*30/100 ), 2)) + ' € \n ▶ Link     : ' + product_link
							})
					
					c_publicados = c_publicados + 1 # Contará la cantidad de products publicados

					# Widget cantidad products publicados

					self.any_signal.emit(c_publicados)						

					if c_publicados == 12:
						break

			g = open ('publish.txt','w+')
			g.writelines("")

			self.any_signal.emit(12)

		except:
			self.any_signal.emit(14)
			

	def stop(self):
		self.is_running = False
		print('Stopping thread...', self.index)
		self.terminate()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	my_app = MainWindow()
	my_app.show()
	sys.exit(app.exec_())
