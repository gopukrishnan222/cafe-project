import os, sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.setGeometry(0,0, 500,650)
        self.setWindowTitle("Debreate")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.resize(500,650)
        self.setMinimumSize(500,650)
        self.center()
        
        # --- Menu --- #
        open = QtGui.QAction("Exit", self)
        save = QtGui.QAction("Save", self)
        build = QtGui.QAction("Build", self)
        exit = QtGui.QAction("Quit", self)
        
        menu_bar = QtGui.QMenuBar()
        file = menu_bar.addMenu("&File")
        help = menu_bar.addMenu("&Help")
        
        file.addAction(open)
        file.addAction(save)
        file.addAction(build)
        file.addAction(exit)
        
        tabs = QtGui.QTabWidget(self)
        tab_bar = QtGui.QTabBar(tabs)
        
        tab_1 = tab_bar.addTab("Main")
        tab_2 = tab_bar.addTab("Description")
        
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(menu_bar)
        vbox.addWidget(tabs)
        
        self.setLayout(vbox)
    
    
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


app = QtGui.QApplication(sys.argv)
frame = MainWindow()
frame.show()
sys.exit(app.exec_())  
