# coding=latin-1

#Python Modules
import sys
import string

#My Modules
from DCMap import World 
from DCRoom import *


class Game(object):
	
	def __init__(self, width, height):
		self.__gameMap = World(width, height, 200, 15)
		self.__commandList = {
				"move" : self.move,"m" : self.move,
				"look" : self.look,"l" : self.look,
				"take" : self.take,"t" : self.take,
				"drop" : self.drop,"d" : self.drop,
				"attack" : self.attack,"a" : self.attack,
				"map" : self.map_,
#				"save" : save,
#				"load" : load,
#				"quit" : quit
		}

		self.__singleCmds = {"look", "map", "quit"}

	#Run command, update game object
	def update(self, command):
		return self.command(command)

	#Parse the command
	def command(self, command):

		try:
			line = string.lower(command).split(" ")
			main = line[0]
			if len(line) > 1:
				mod = line [1:]
			elif main in self.__singleCmds:
				mod = None
			else:
				return "Incomplete command: " + command

			try:
				return self.__commandList[main](mod)
			except KeyError:
				return "Command Borked"
 		except ValueError:
			raise ValueError

			

	def move(self, direction):
		curRoom = self.__gameMap.getCurrentRoom()

		directions = {
			"n" : curRoom.getNorth(), "north" : curRoom.getNorth(),
			"e" : curRoom.getEast(), "east" : curRoom.getEast(),
			"s" : curRoom.getSouth(), "south" : curRoom.getSouth(),
			"w" : curRoom.getWest(), "west" : curRoom.getWest()
		}
		try:
			nextRoom = directions[direction[0]]
		except KeyError:
			return "Invalid direction: " + direction[0]
		try:
			if nextRoom is not None and nextRoom is not -1:
				self.__gameMap.setCurrentRoom(nextRoom)
				return "You moved: " + direction[0]
			else:
				return "No room in direction: " + direction[0]
		except Exception, err:
			return unicode(err)


	def look(self, object_):
		if object_ is not None:
			return "You looked at: " + object_[0]
		else:
			return "You looked at the room"

	def take(self, item):
		return "You took: " + item[0]

	def drop(self, item):
		return "You dropped: " + item[0]

	def attack(self, enemy):
		return "You attacked: " + enemy[0]

	def map_(self, type_):
		return self.__gameMap 

