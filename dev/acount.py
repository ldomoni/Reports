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

	def cancel_item(self, description, quantity, unit_price):
		item_to_cancel = Item(description, quantity, unit_price)

		for item in self._items:
			if item.is_item_equal(item_to_cancel):
				item.item_cancel(item_to_cancel)

class Item(object):
	def __init__(self, description, quantity, unit_price):
		
		if unit_price <= 0 or quantity <= 0:
			raise Exception('')

		self._description = description
		self._unit_price = unit_price
		self._quantity = quantity

	def get_item_amount(self):
		return self._unit_price * self._quantity

	def is_item_equal(self, other_item):
		if self._description == other_item._description and self._unit_price == other_item._unit_price:
			return True

		return False

	def item_cancel(self, item_to_cancel):
		new_quantity= self._quantity - item_to_cancel._quantity
				
		if new_quantity >= 0:
			self._quantity = new_quantity
		else:
			raise Exception('')


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