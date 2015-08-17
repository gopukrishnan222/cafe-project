import sys
from PyQt4 import QtGui
import socket
#import time

class ping():
	"""To ping computers"""
	def __init__(self, ip,name, movex , movey , obj ,status="off"):
		self.ip = ip
		self.name = name
		self.obj = obj
		self.s =  socket.socket ()
		self.s.settimeout (0.25)

		self.img = str(self.name) + str(status) + '.png'
		self.movex = movex
		self.movey = movey
		self.setImage('off')
		self.setLabel()
		self.ping()

		
	
	def ping(self):
		try:
			self.s.connect ((self.ip, 135))
		except socket.error:
			self.setImage('off')
		else:
			self.setImage('on')
		self.s.close()
		self.setLabel()
	
	def setLabel(self):
		pixmap = QtGui.QPixmap(self.img)
		self.lbl = QtGui.QLabel(self.obj)
		self.lbl.setPixmap(pixmap)
		#hbox.addWidget(self.lbl)
		#self.setLayout(hbox)
		self.lbl.move(self.movex,self.movey)
		self.lbl.resize(120,70)


	def setImage(self,st):
		self.img = str(self.name) + (st) + '.png'


		
class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()  # SELF CAN REPLACE THE COMMAND WINDOW INSIDE CLASS WINDOW. EG. SELF.SHOW()  for   WINDOW.SHOW()
		self.setGeometry(200,100, 900, 600)  # WINDOW SIZE
		self.setWindowTitle("Radha Communications")   # WINDOW TITLE
		self.setWindowIcon(QtGui.QIcon('LED.png'))   # LOGO AT TOP LEFT CORNER


		
		Exit = QtGui.QAction("Exit", self) # ADDING EXIT BUTTON IN FILE MENU
		Exit.setShortcut("Ctrl+Q")         # SETTING SHORTCUT
		Exit.setStatusTip('Close The Window')
		Exit.triggered.connect(self.close_application)

		Info = QtGui.QAction("Info", self)    #ADDING INFO BUTTON
		Info.setShortcut("Ctrl+I")
		Info.setStatusTip('Information')
		#Info.triggered.connect( )


		Aboutus = QtGui.QAction("About us", self)    #ADDING About us BUTTON
		Aboutus.setStatusTip('About Us')
		#Aboutus.triggered.connect( )

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(Exit)
		

		HelpMenu = mainMenu.addMenu('Help')
		HelpMenu.addAction(Info)
		HelpMenu.addAction(Aboutus)

		##  pc
		
		#-*while True:
		pc0 = ping("192.168.1.19","pc0",50,90, self)
#25
		pc1 = ping("192.168.0.172","pc1",200,90, self)
		
#24
		pc2 = ping("192.168.0.127","pc2",350,90,self)
		
#23
		pc3 = ping("192.168.0.38","pc3",50,180,self)

#22
		pc4 = ping("192.168.0.114","pc4",200,180,self)
		
#21
		pc5 = ping("192.168.0.128","pc5",350,180,self)
		
#20
		pc6 = ping("192.168.0.20","pc6",50,270,self)
		
#19
		pc7 = ping("192.168.0.152","pc7",200,270,self)
		
#18
		pc8 = ping("192.168.0.153","pc8",350,270,self)
		
#17
		pc9 = ping("192.168.0.2","pc9",50,360,self)
		

#16
		pc10 = ping("192.168.0.128","pc10",200,360,self)

#15
		pc11 = ping("192.168.0.128","pc11",350,360,self)

#14
		pc12 = ping("192.168.0.11","pc12",50,450,self)

#13
		pc13 = ping("192.168.0.11","pc13",200,450,self)

#12
		pc14 = ping("192.168.0.11","pc14",350,450 ,self)

		
		
		

	def close_application(self):            # Close Conformation
		choice = QtGui.QMessageBox.question(self, 'Exit!',
											"Are you really want to quit",
											QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			print("Exit")
			sys.exit()
		else:
			pass

		
		#self.show() #MUST BE ADDED TO SHOW WINDOW
		
		# ADDING MENU BAR ITEMS
		#time.sleep(1)
			
		

	

		
		

		
			


	
	



	



##-------------------------------------------------------------------------------------------------
		
app = QtGui.QApplication(sys.argv)  #DEFINE THE APP
GUI = Window()          #CALLING THE CLASS WINDOW
GUI.show()
GUI.statusBar()
sys.exit(app.exec_())
