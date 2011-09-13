# coding=latin-1

#Python modules
import random

#My Modules
from DCRoom import Room


class World(object): 
	def __init__(self, width, length, numRooms, density):
		self.__width = width
		self.__length = length
		self.__numRooms = numRooms
		self.__density = density
		
		self.__worldMap = [[Room((x+1)*(y+1), x, y) for x in range(0,self.__width)] for y in range(0,self.__length)]
#		self.__worldMap[4][5].setWest(self.__worldMap[4][4])
#		self.__worldMap[4][5].setNorth(self.__worldMap[3][5])
#		self.__worldMap[5][5].setNorth(self.__worldMap[4][5])
#		self.__worldMap[5][6].setWest(self.__worldMap[5][5])
#		self.__currentRoom = self.__worldMap[5][6]
		self._populateWorld(40)

	#private functions

	def _populateWorld(self, numRooms):
		for n in range (0,self.__width):
			self.getRoom(n,0).setNorth(-1)
			self.getRoom(n,self.__length-1).setSouth(-1)
		for n in range(0,self.__length):
			self.getRoom(0,n).setWest(-1)
			self.getRoom(self.__width-1,n).setEast(-1)

		widthWindow = int(.25 * self.__width)
		halfWidth = int(self.__width / 2)
		lengthWindow = int(.25 * self.__length)
		halfLength = int(self.__length / 2)
		startX = random.randint(halfWidth - widthWindow, halfWidth + widthWindow)
		startY = random.randint(halfLength - lengthWindow, halfLength + lengthWindow)
		self.setCurrentRoom(self.getRoom(startX,startY))

		#Sets up some rooms next to the start room. Required for map population.
		#If no rooms are set, it defaults to a room to the east
		if random.randint(0,1) is 1:
			self.getRoom(startX,startY-1).setSouth(self.getCurrentRoom())
		if random.randint(0,1) is 1:
			self.getRoom(startX+1,startY).setWest(self.getCurrentRoom())
		if random.randint(0,1) is 1:
			self.getRoom(startX,startY+1).setNorth(self.getCurrentRoom())
		if random.randint(0,1) is 1:
			self.getRoom(startX-1,startY).setEast(self.getCurrentRoom())
		if self.getCurrentRoom().getNeighbors is 0:
			self.getRoom(startX+1,startY).setWest(self.getCurrentRoom())


		roomsLeft = self.__numRooms
		hangUps = 0
		while roomsLeft > 0 and hangUps < self.__numRooms:
			x = random.randint(1,self.__width-2)
			y = random.randint(1,self.__length-2)
			

			setRoom = False
			if self.neighborsOfNeighbors(self.getRoom(x,y)) < self.__density:
				if self.getRoom(x,y-1).getNeighbors() > 0:
					self.getRoom(x,y).setNorth(self.getRoom(x,y-1))
					setRoom = True
				if self.getRoom(x+1,y).getNeighbors() > 0:
					self.getRoom(x,y).setEast(self.getRoom(x+1,y))
					setRoom = True
				if self.getRoom(x,y+1).getNeighbors() > 0:
					self.getRoom(x,y).setSouth(self.getRoom(x,y+1))
					setRoom = True
				if self.getRoom(x-1,y).getNeighbors() > 0:
					self.getRoom(x,y).setWest(self.getRoom(x-1,y))
					setRoom = True
				if setRoom:
					roomsLeft -= 1
			else:
				hangUps += 1
		print roomsLeft

				
	#This isn't really useful I don't think but it checks if the room's neighbors have neighbors.				
	def neighborsOfNeighbors(self,room):
		x = room.getXCoord()
		y = room.getYCoord()

		neighbors = 0
		neighbors += self.getRoom(x,y-1).getNeighbors()
		neighbors += self.getRoom(x+1,y).getNeighbors()
		neighbors += self.getRoom(x,y+1).getNeighbors()
		neighbors += self.getRoom(x-1,y).getNeighbors()
		
		return neighbors

	#Get Functions
	def getCurrentRoom(self):
		return self.__currentRoom
	def getRoom(self,x,y):
		return self.__worldMap[y][x]


	def _getRoomChar(self, room):
		nei = room.getNeighbors()
		roomChars ={8: "▀", 2: "▄", 10: "│",
					4: "■", 1: "■", 5: "─",
					12: "└", 6: "┌", 3: "┐", 9: "┘",
					14: "├", 7: "┬", 11: "┤", 13: "┴",
					15: "┼", 0: "░"} # ░
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
					mapString += self._getRoomChar(r)
			mapString += "║\r\n"
		mapString += "╚"
		for n in range(0,self.__width):
			mapString += "═"
		mapString += "╝"
		return unicode(mapString, "utf-8")
