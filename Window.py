# coding=latin-1

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Window(QDialog):
	def __init__(self, Game, parent=None):
		super(Window, self).__init__(parent)
		
		self.game = Game

		#create widgets
		self.textBox = QTextEdit()
		self.cmdLine = QLineEdit()
		self.button = QPushButton("Do it")
		
		#Set up layout
		layout = QGridLayout()
		layout.addWidget(self.textBox,0,0,1,2)
		layout.addWidget(self.cmdLine,1,0)
		layout.addWidget(self.button,1,1)
		layout.setSizeConstraint(QLayout.SetFixedSize)
		self.setLayout(layout)

		#set up the Window
		self.setWindowTitle("Dungeon Crawler")
		self.setSizeGripEnabled(False)

		#set up the text box
		self.textBox.setLineWidth(80)
		self.textBox.setReadOnly(True)
		self.textBox.setFontFamily("monospace")
		self.textBox.setMinimumSize(QSize(740,400))

		#set up command line
		self.cmdLine.setFocus()

		#Setup connections
		self.connect(self.cmdLine, SIGNAL("returnPressed()"), self.button, SLOT("animateClick(100)"))
		self.connect(self.button, SIGNAL("clicked()"), self.updateUi)

	def updateUi(self):
		try:
			text = unicode(self.cmdLine.text())
			gameState = unicode(self.game.update(text))
			self.textBox.clear()
			self.textBox.append(gameState)
			self.cmdLine.clear()
		except Exception, err:
			self.textBox.append("Invalid Command: " + text)
			self.textBox.append(unicode(err))
			self.cmdLine.clear()
	
