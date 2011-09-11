class Room(object):

	def __init__(self, idNum, north=None, east=None, south=None, west=None):
		self.__idNum = idNum
		self.__north = None
		self.__south = None
		self.__east = None
		self.__west = None
		self.setNorth(north) 
		self.setEast(east)
		self.setSouth(south)
		self.setWest(west)
		
#	Set functions
	def setNorth(self, room, init=1):
		if self.__north is not None:
			self.__north.remSouth()
		self.__north = room
		if room is not None:
			if init is 1:
				room.setSouth(self, 0)
	def setEast(self, room, init=1):
		if self.__east is not None:
			self.__east.remWest()
		self.__east = room
		if room is not None:
			if init is 1:
				room.setWest(self, 0)
	def setSouth(self, room, init=1):
		if self.__south is not None:
			self.__south.remNorth()
		self.__south = room
		if room is not None:
			if init is 1:
				room.setNorth(self, 0)
	def setWest(self, room, init=1):
		if self.__west is not None:
			self.__west.remEast()
		self.__west = room
		if room is not None:
			if init is 1:
				room.setEast(self, 0)

#	Get Functions
	def getIDNum(self):
		return self.__idNum
	def getNorth(self):
		return self.__north
	def getEast(self):
		return self.__east
	def getSouth(self):
		return self.__south
	def getWest(self):
		return self.__west
	#returns a binary number representing where there are neighbors
	def getNeighbors(self):
		neighbors = 0
		if self.getNorth() is not None:
			neighbors += 0b1000
		if self.getEast() is not None:
			neighbors += 0b0100
		if self.getSouth() is not None:
			neighbors += 0b0010
		if self.getWest() is not None:
			neighbors += 0b0001
		return neighbors

	#Functions for removing neighbors
	def remNorth(self):
		self.__north = None
	def remEast(self):
		self.__east = None
	def remSouth(self):
		self.__south = None
	def remWest(self):
		self.__west = None


	#compare
	def __cmp__(self,other):
		return cmp(self.__idNum, other.getIDNum())

	def __unicode__(self):
		return "ID Number: " + unicode(self.getIDNum())
