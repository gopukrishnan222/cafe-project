#gk
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import socket
import time

class worker(QThread):
	
	signal = pyqtSignal(str, list)
	
	def __init__(self,ip,name,movex,movey):
		QThread.__init__(self, parent=app)
		
		#print("\t\t\t\nNew Thread\n")
		self.ip = ip
		self.name = name

		self.movex = movex
		self.movey = movey

	def run(self):
		self.active = True

		while self.active:			# Comment while loop to ping all PC's only once
			print ('Ping '+str(self.name)+' '+str(self.ip))
			try:
				self.s =  socket.socket ()
				self.s.settimeout (0.25)		# Max time limit for pinging
				self.s.connect ((self.ip, 135))
			except socket.error as e:
				print('Exception: '+str(self.name)+' '+str(self.ip)+', '+str(e))
				self.signal.emit(self.name+"off.png", [self.movex,self.movey])
			else:
				self.signal.emit(self.name+"on.png", [self.movex,self.movey])
			self.s.close()
			time.sleep(10)
		
class Window(QMainWindow):

	def __init__(self):
		super(Window, self).__init__()  # SELF CAN REPLACE THE COMMAND WINDOW INSIDE CLASS WINDOW. EG. SELF.SHOW()  for   WINDOW.SHOW()


		
		self.setGeometry(200,100, 900, 600)  # WINDOW SIZE
		self.setWindowTitle("Radha Communications")   # WINDOW TITLE
		self.setWindowIcon(QIcon('LED.png'))   # LOGO AT TOP LEFT CORNER
		
		Exit = QAction("Exit", self) # ADDING EXIT BUTTON IN FILE MENU
		Exit.setShortcut("Ctrl+Q")         # SETTING SHORTCUT
		Exit.setStatusTip('Close The Window')
		Exit.triggered.connect(self.close_application)

		Info = QAction("Info", self)    #ADDING INFO BUTTON
		Info.setShortcut("Ctrl+I")
		Info.setStatusTip('Information')
		
		Aboutus = QAction("About us", self)    #ADDING About us BUTTON
		Aboutus.setStatusTip('About Us')
		
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(Exit)
		

		HelpMenu = mainMenu.addMenu('Help')
		HelpMenu.addAction(Info)
		HelpMenu.addAction(Aboutus)

		##  pc
		self.threads = []
		
		self.pc = [\
		"192.168.1.10",
		"192.168.1.19",
		"192.168.0.127",
		"192.168.0.38",
		"192.168.0.114",
		"192.168.0.128",
		"192.168.0.20",
		"192.168.0.152",
		"192.168.0.128",
		"192.168.0.20",
		"192.168.0.152",
		"192.168.0.153"\
		]

		# x_cord = [50,200,350]
		# y_cord = [90,180,270,360]
		
		pc_cntr = 0
		# xc = 0
		# yc = 0

		
			
			# if xc == 3:
			# 	xc = 0
			# if yc == 4:
			# 	yc = 0

		for yc in [90,180,270,360]:
			for xc in [50,200,350]:
				ip=self.pc[pc_cntr]
				
				pc_name = 'pc'+str(pc_cntr)
				print (xc,yc,pc_name)
				self.ping( ip, pc_name , xc, yc)
		
				pc_cntr += 1
			# xc += 1
			# yc += 1




	
	def ping(self,ip,name, movex , movey):
		thread = worker(ip,name,movex,movey)
		thread.signal.connect(self.showStatus)
		thread.start()
		self.threads.append(thread)

	def showStatus(self, img,cord):
		pixmap = QPixmap(img)
		icon = QLabel(self)
		icon.setPixmap(pixmap)
		icon.move(cord[0],cord[1])
		icon.resize(120,70)
		icon.show()


	def close_application(self):            # Close Conformation
		choice = QMessageBox.question(self, 'Exit!',
											"Do you really want to quit",
											QMessageBox.Yes | QMessageBox.No)
		if choice == QMessageBox.Yes:
			print("\n\n\tWaiting for threads to stop. . \n\n")
			

			for t in self.threads:
				t.active = False
				t.quit()
				t.wait(1000)
				
			sys.exit()
		else:
			pass

##-------------------------------------------------------------------------------------------------
		
app = QApplication(sys.argv)  #DEFINE THE APP
GUI = Window()          #CALLING THE CLASS WINDOW
GUI.show()
GUI.statusBar()
sys.exit(app.exec_())
