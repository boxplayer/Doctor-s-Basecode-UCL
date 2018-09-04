import os
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QCheckBox, QApplication,QFileDialog, QPushButton, QWidget, QLineEdit, QLabel, QListWidget, QPlainTextEdit)
from PyQt5.QtGui import QFont



class Button(QPushButton):
  
	def __init__(self, title, parent):
		super().__init__(title, parent)
		
	def wiki_click(self):

		print("current snomed:".format(self._current_snomed))



class UploadWindow(QWidget):
  
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):

		edit = QLineEdit('', self)
		edit.setDragEnabled(True)
		edit.setReadOnly(True)
		edit.move(20, 20)
		edit.isReadOnly()
		self.edit = edit
		self.articles_checked = None
		self.wikipedia_checked = None

		self.checkbox = QCheckBox("Download Articles",self)
		self.checkbox.move(15, 50)
		self.checkbox.stateChanged.connect(self.clickBoxArticles)

		self.checkbox = QCheckBox("Wikipedia Descriptions",self)
		self.checkbox.move(15, 70)
		self.checkbox.stateChanged.connect(self.clickBoxWikipedia)

		button = Button("Choose file", self)
		button.move(138, 16)
		button.clicked.connect(self.upload_pdf)

		button2 = Button("Run", self)
		button2.setEnabled(False)
		button2.move(180, 45)
		button2.clicked.connect(self.exit)
		self.button2 = button2
		
		self.setWindowTitle('cTAKES Program')
		self.setGeometry(700, 300, 280, 100)

	def clickBoxArticles(self, state):
		if state == QtCore.Qt.Checked:
			print("articles checked")
			self.articles_checked = True
		else:
			print("articles unchecked")
			self.articles_checked = False

	def clickBoxWikipedia(self, state):
		if state == QtCore.Qt.Checked:
			print("wiki checked")
			self.wikipedia_checked = True
		else:
			print("wiki unchecked")
			self.wikipedia_checked = False

	def upload_pdf(self):
		dialog = QFileDialog()
		fname = dialog.getOpenFileName(None, "Import PDF", "", "PDF data file (*.pdf)")
		# if(isEmpty(fname[0]) == False):
		self.fname = fname[0]
		self.edit.setText(os.path.basename(fname[0]))
		self.button2.setEnabled(True)



	def exit(self):
		self.close()
		# sys.exit(app.exec_())


class WikiWindow(QWidget):
  
	def __init__(self, name, wikipedia_description):
		super().__init__()
		

		self.initUI(name, wikipedia_description)
		
		
	def initUI(self,name, wikipedia_description):

		box = QPlainTextEdit(wikipedia_description, self)
		box.setReadOnly(True)
		box.setGeometry(10,10,475,270)
		
		self.setWindowTitle('Wikipedia: {}'.format(name))
		self.setGeometry(300, 100, 500, 300)

class ArticleWindow(QWidget):
  
	def __init__(self, name, medical_articles):
		super().__init__()
		

		self.initUI(name, medical_articles)
		
		
	def initUI(self,name, medical_articles):

		if(medical_articles is None):
			self.close()
			return

		box = QPlainTextEdit(" ", self)
		box.setReadOnly(True)
		box.setGeometry(10,10,475,470)
		
		for article in medical_articles:
			box.appendPlainText("--UID: {}".format(article['uid']))
			box.appendPlainText("--Date: {}".format(article['pubdate']))
			box.appendPlainText("--Last Author: {}".format(article['lastauthor']))
			box.appendPlainText("--Title: {}".format(article['title']))
			box.appendPlainText("\n \n")

		self.setWindowTitle('Articles: {}'.format(name))
		self.setGeometry(300, 200, 500, 500)




class Label(QLabel):
	def __init__(self, title, parent):
		super().__init__(title, parent)

class CurrentSNO:
	def __init__(self, snomed_name):
		self._snomed_name = snomed_name
	def name():
		return self._snomed_name

class List(QListWidget):

	def __init__(self, parent, _list, snomed_code):
		super().__init__(parent)
		self.itemClicked.connect(self.item_click)
		self._list = _list
		self._snomed_label = snomed_code

	def item_click(self, item):
		print("item!: ", item.text())
		for entity in self._list:
			if (entity.name() == item.text()):
				snomed_term = entity.snomed_code()
				self._snomed_label.setText(entity.snomed_code())
				return

	# @staticmethod
	# def get_name():
	# 	return snomed_name

class DisplayWindow(QWidget):
	

	def __init__(self, summary, filename):
		super().__init__()
		
		self.initUI(summary, filename)

	def wiki_click(self, summary):

		print("current snomed: {}".format(self.snomedlabel.text()))

		# get summary class
		self.summary = summary

		# extract lists from class
		medlist = self.summary.get_medicine_list()
		symlist = self.summary.get_symptom_list()
		analist = self.summary.get_anatomy_list()
		prolist = self.summary.get_procedure_list()
		dislist = self.summary.get_disease_list()

		fullist = [medlist, symlist, analist, prolist, dislist]
		for onelist in fullist:
			for entity in onelist:
				if entity.snomed_code() == self.snomedlabel.text():
					print("Wikipedia description: ", entity.wikipedia_description())
					# open display gui to show information
					self.wiki = WikiWindow(entity.name(), entity.wikipedia_description())
					self.wiki.show()  

					return

	def article_click(self, summary):

		print("current snomed: {}".format(self.snomedlabel.text()))

		# get summary class
		self.summary = summary

		# extract lists from class
		medlist = self.summary.get_medicine_list()
		symlist = self.summary.get_symptom_list()
		analist = self.summary.get_anatomy_list()
		prolist = self.summary.get_procedure_list()
		dislist = self.summary.get_disease_list()

		fullist = [medlist, symlist, analist, prolist, dislist]
		for onelist in fullist:
			for entity in onelist:
				if entity.snomed_code() == self.snomedlabel.text():
					# open display gui to show information
					self.article = ArticleWindow(entity.name(), entity.medical_articles())
					self.article.show()  

					return



		
	def initUI(self,summary, filename):

		# get summary class
		self.summary = summary
		self.filename = filename

		# extract lists from class
		medlist = self.summary.get_medicine_list()
		symlist = self.summary.get_symptom_list()
		analist = self.summary.get_anatomy_list()
		prolist = self.summary.get_procedure_list()
		dislist = self.summary.get_disease_list()

		# FILE LABEL
		filelabel = Label('', self)
		filename2 = "File: " + filename
		filelabel.setText(filename2)
		filelabel.move(400, 50)

		# SNOMED NAME
		filelabel = Label('SNOMED: ', self)
		filelabel.move(380, 80)
		filelabel2 = QLineEdit('', self) 
		filelabel2.setReadOnly(True) 
		filelabel2.setGeometry(444, 79, 90, 20)
		self.snomedlabel = filelabel2

		# CLOSE BUTTON
		button2 = Button("Close", self)
		button2.move(480, 10)
		button2.clicked.connect(self.exit)

		# WIKIPEDIA BUTTON
		button2 = Button("Wikipedia", self)
		button2.move(435, 100 )
		# button2.setEnabled(False)
		button2.clicked.connect(lambda: self.wiki_click(summary))
		self._button2 = button2

		# ARTICLES BUTTON
		button3 = Button("Articles", self)
		button3.move(435, 123 )
		# button2.setEnabled(False)
		button3.clicked.connect(lambda: self.article_click(summary))
		self._button3 = button3


		myFont=QFont()
		myFont.setBold(True)


		# MEDICINE LABEL
		filelabel = Label('MEDICINE ', self)
		filelabel.setFont(myFont)
		filelabel.move(11, 30)

		# POPULATE MEDICINE LISTBOX
		list_widget_med = List(self, medlist, self.snomedlabel)
		list_widget_med.resize(180,275)
		list_widget_med.show()
		list_widget_med.setGeometry(10, 50, 180, 275)
		for entity in medlist:
			list_widget_med.addItem(entity.name())


		# SYMPTOM LABEL
		filelabel = Label('SYMPTOMS ', self)
		filelabel.setFont(myFont)
		filelabel.move(191, 30)

		# POPULATE SYMPTOM LISTBOX
		list_widget_sym = List(self, symlist, self.snomedlabel)
		list_widget_sym.resize(180,275)
		list_widget_sym.show()
		list_widget_sym.setGeometry(190, 50, 180, 275)
		for entity in symlist:
			list_widget_sym.addItem(entity.name())


		# ANATOMY LABEL
		filelabel = Label('ANATOMY ', self)
		filelabel.setFont(myFont)
		filelabel.move(11, 330)

		# POPULATE ANATOMY LISTBOX
		list_widget_ana = List(self, analist, self.snomedlabel)
		list_widget_ana.resize(180,275)
		list_widget_ana.show()
		list_widget_ana.setGeometry(10, 350, 180, 275)
		for entity in analist:
			list_widget_ana.addItem(entity.name())



		# PROCEDURE LABEL
		filelabel = Label('PROCEDURES ', self)
		filelabel.setFont(myFont)
		filelabel.move(191, 330)

		# POPULATE PROCEDURE LISTBOX
		list_widget_pro = List(self, prolist, self.snomedlabel)
		list_widget_pro.resize(180,275)
		list_widget_pro.show()
		list_widget_pro.setGeometry(190, 350, 180, 275)
		for entity in prolist:
			list_widget_pro.addItem(entity.name())



		# DISEASE/DISORDER LABEL
		filelabel = Label('DISEASES/DISORDERS ', self)
		filelabel.setFont(myFont)
		filelabel.move(371, 330)

		# POPULATE DISEASE/DISORDER LISTBOX
		list_widget_dis = List(self, dislist, self.snomedlabel)
		list_widget_dis.resize(180,275)
		list_widget_dis.show()
		list_widget_dis.setGeometry(370, 350, 180, 275)
		for entity in dislist:
			list_widget_dis.addItem(entity.name())




		# WINDOW FORMAT
		self.setWindowTitle('cTAKES Program')
		self.setGeometry(600, 800, 560, 650)
		
	def exit(self):
		self.close()
		# sys.exit(app.exec_())