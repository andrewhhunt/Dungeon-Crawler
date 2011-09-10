# coding=latin-1

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Window import *
from Game import *

app = QApplication(sys.argv)
game = Game()
window = Window(game)
window.show()
app.exec_()
