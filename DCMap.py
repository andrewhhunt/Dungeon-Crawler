# coding=latin-1

#Python modules
import random

#My Modules
from DCRoom import Room


class World(object): 
	def __init__(self, width, length):
		self.__width = width
		self.__length = length
		
		self.__worldMap = [[Room((x+1)*(y+1)) for x in range(0,width)] for y in range(0,length)]
		self.__worldMap[4][5].setWest(self.__worldMap[4][4])
		self.__worldMap[4][5].setNorth(self.__worldMap[3][5])
		self.__worldMap[5][5].setNorth(self.__worldMap[4][5])
		self.__worldMap[5][6].setWest(self.__worldMap[5][5])
		self.__currentRoom = self.__worldMap[5][6]

	#Get Functions
	def getCurrentRoom(self):
		return self.__currentRoom


	def getRoomChar(self, room):
		nei = room.getNeighbors()

		roomChars ={8: "▀", 2: "▄", 10: "│",
					4: "■", 1: "■", 5: "─",
					12: "└", 6: "┌", 3: "┐", 9: "┘",
					14: "├", 7: "┬", 11: "┤", 13: "┴",
					15: "┼", 0: " "}
		return roomChars[nei]


	#set functions
	def setCurrentRoom(self, room):
		self.__currentRoom = room

	#default functions
	def __unicode__(self):
		mapString = "╔══ MAP "
		for n in range(0,self.__width - 7):
			mapString += "═"
		mapString += "╗\r\n"
		for row in self.__worldMap:
			mapString += "║"
			for r in row:
				if r is self.getCurrentRoom():
						mapString += "◊"
				else:
					mapString += self.getRoomChar(r)
			mapString += "║\r\n"
		mapString += "╚"
		for n in range(0,self.__width):
			mapString += "═"
		mapString += "╝"
		return unicode(mapString, "utf-8")
