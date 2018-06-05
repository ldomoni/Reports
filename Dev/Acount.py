from Item import  *

class Acount(object):
	def __init__(self, name_acount):
		self.__name = name_acount
		self.__items = []

	def __eq__(self, other_acount):
		if self.__name == other_acount.__name:
			return True
		return False
	"""
	Public methods.
	"""

	def get_name_acount(self):
		return self.__name

	def get_acount_amount(self):
		return sum([item.get_item_amount() for item in self.__items])
	
	def add_item(self, description, amount):
		self.__items.append(ItemAcount(description, amount))
