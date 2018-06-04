from Acount import  *

class Journal(object):
	def __init__(self):
		self.__acounts= []

	"""
	Public methods.
	"""

	def get_journal_amount(self):
		return sum([acount.get_acount_amount() for acount in self.__acounts]) 

	def add_acount(self, name_acount):
		self.__acounts.append(Acount(name_acount))
	
	def get_number_acounts(self):
		return len(self.__acounts)

	def get_acount(self, name_acount):
		for acount in self.__acounts:
			if acount.get_name_acount() == name_acount:
				return acount