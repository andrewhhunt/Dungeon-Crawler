# coding=latin-1

import sys
import string


class Game(object):
	def __init__(self):
		stuff = 3

	def update(self, command):
		return self.command(command)

	def command(self, command):
		try:
			line = string.lower(command).split(" ")
			main = line[0]
			if line[1]:
				mod = line [1:]
			else:
				raise ValueError
		
			commands = {
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
		
			try:
				return commands[main](mod)
			except:
				return  "That shit broke"

 		except:
			return "Invalid command!"

			

	def move(self, direction):
		return "You moved in the following direction: " + unicode(direction[0])

	def look(self, object_):
		return "You looked at: " + object_[0]

	def take(self, item):
		return "You took: " + item[0]

	def drop(self, item):
		return "You dropped: " + item[0]

	def attack(self, enemy):
		return "You attacked: " + enemy[0]

	def map_(self, nothing):
		return unicode(open("map.txt").read(),"utf-8") 
