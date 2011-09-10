# coding=latin-1

import sys
import game
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import window

app = QApplication(sys.argv)
gameObj = game.gameWorld()
window = window.Window(gameObj)
window.show()
app.exec_()
