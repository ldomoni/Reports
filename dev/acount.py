class Acount(object):
	def __init__(self, name_acount):
		self._name = name_acount
		self._items = []

	"""
	Public methods.
	"""

	def get_name_acount(self):
		return self._name

	def get_acount_amount(self):
		return sum([item.get_item_amount() for item in self._items])
	
	def add_item(self, description, unit_price, quantity):
		self._items.append(Item(description, unit_price, quantity))


class Item(object):
	def __init__(self, description, quantity, unit_price):
		self._description = description
		self._unit_price = unit_price
		self._quantity = quantity

	def get_item_amount(self):
		return self._unit_price * self._quantity


class Journal(object):
	def __init__(self):
		self._acounts= []

	def get_journal_amount(self):
		return sum([acount.get_acount_amount() for acount in self._acounts]) 

	def add_acount(self, name_acount):
		self._acounts.append(Acount(name_acount))
	
	def get_number_acounts(self):
		return len(self._acounts)

	def get_acount(self, name_acount):
		for acount in self._acounts:
			if acount.get_name_acount() == name_acount:
				return acount