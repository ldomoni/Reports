from Acount import  *

class Journal(object):
	def __init__(self):
		self.__acounts= []
	
	"""
	Private methods.
	"""

	def __get_acount(self, name_acount):
		for acount in self.__acounts:
			if acount.get_name_acount() == name_acount:
				return acount

	"""
	Public methods.
	"""

	def get_journal_amount(self):
		return sum([acount.get_acount_amount() for acount in self.__acounts]) 

	def add_acount(self, name_acount):
		self.__acounts.append(Acount(name_acount))
	
	def add_item_acount(self, name_acount, description, amount):
		acount= self.__get_acount(name_acount)
		acount.add_item(description, amount)

	def get_number_acounts(self):
		return len(self.__acounts)

	def is_acount_in_journal(self, name_acount):
		acount = self.__get_acount(name_acount)

		if acount:
			return True

		return False