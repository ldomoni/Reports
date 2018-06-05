class Item(object):
	def __init__(self, description, quantity, unit_price):
		self.__description = description
		self.__unit_price = unit_price
		self.__quantity = quantity

	"""
	Public methods.
	"""

	def get_item_amount(self):
		return self.__unit_price * self.__quantity

	def get_description(self):
		return self.__description

	def get_quantity(self):
		return self.__quantity

	def get_unit_price(self):
		return self.__unit_price

class ItemAcount(Item):
	def __init__(self, description, amount):
		super(ItemAcount, self).__init__(description, 1, amount)
