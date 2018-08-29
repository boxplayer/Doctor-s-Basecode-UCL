import os
from PyQt5.QtWidgets import (QFileDialog, QPushButton, QWidget, QLineEdit, QLabel, QListWidget)
from PyQt5.QtGui import QFont

class Button(QPushButton):
  
	def __init__(self, title, parent):
		super().__init__(title, parent)
		
class Label(QLabel):
	def __init__(self, title, parent):
		super().__init__(title, parent)

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
				self._snomed_label.setText(entity.snomed_code())


		# self.snomedlabel.setText("LOLZ")




class UploadWindow(QWidget):
  
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):

		edit = QLineEdit('', self)
		edit.setDragEnabled(True)
		edit.setReadOnly(True)
		edit.move(20, 30)
		edit.isReadOnly()
		self.edit = edit

		button = Button("Choose file", self)
		button.move(138, 26)
		button.clicked.connect(self.upload_pdf)

		button2 = Button("Run", self)
		button2.setEnabled(False)
		button2.move(180, 55)
		button2.clicked.connect(self.exit)
		self.button2 = button2
		
		self.setWindowTitle('cTAKES Program')
		self.setGeometry(700, 300, 280, 100)

	def exit(self):
		self.close()
		# sys.exit(app.exec_())
	

	def upload_pdf(self):
		dialog = QFileDialog()
		fname = dialog.getOpenFileName(None, "Import PDF", "", "PDF data file (*.pdf)")
		# if(isEmpty(fname[0]) == False):
		self.fname = fname[0]
		self.edit.setText(os.path.basename(fname[0]))
		self.button2.setEnabled(True)

class DisplayWindow(QWidget):
	
	def __init__(self, summary, filename):
		super().__init__()
		
		self.initUI(summary, filename)
		
		
	def initUI(self,summary, filename):

		# CLOSE BUTTON
		button2 = Button("Close", self)
		button2.move(480, 10)
		button2.clicked.connect(self.exit)

		# FILE LABEL
		filelabel = Label('', self)
		filename2 = "File: " + filename
		filelabel.setText(filename2)
		filelabel.move(400, 50)


		# FILE LABEL
		filelabel = Label('SNOMED: ', self)
		filelabel.move(380, 80)

		# FILE LABEL
		filelabel2 = QLineEdit('', self) 
		filelabel2.setReadOnly(True) 
		filelabel2.setGeometry(444, 79, 90, 20)
		# filelabel2 = Label('4945893340', self)
		# filelabel2.move(444, 79)
		self.snomedlabel = filelabel2

		myFont=QFont()
		myFont.setBold(True)

		# get summary class
		self.summary = summary
		self.filename = filename

		# extract lists from class
		medlist = self.summary.get_medicine_list()
		symlist = self.summary.get_symptom_list()
		analist = self.summary.get_anatomy_list()
		prolist = self.summary.get_procedure_list()
		dislist = self.summary.get_disease_list()


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