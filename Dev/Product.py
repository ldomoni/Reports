class Product(object):

	def __init__(self, name_product, stock, alert_stock):
		self.__name= name_product
		self.__stock= stock
		self.__alert_stock= alert_stock

		if stock > alert_stock:
			self.__alert= False
		else:
			self.__alert= False

	def __eq__(self, other_product):
		if self.__name == other_product.__name:
			return True

		return False
	
	"""
	Private methods.
	"""	

	def __set_stock_alert(self):
		if self.__stock <= self.__alert_stock:
			self.__alert= True
		
		else:
			self.__alert= False 

	"""
	Public methods.
	"""

	def get_stock_alert(self):
		return self.__alert_stock

	def get_alert(self):
		return self.__alert

	def get_name_product(self):
		return self.__name
	
	def get_stock(self):
		return self.__stock

	def del_stock(self, quantity_stock):
		if not quantity_stock <= self.__stock:
			raise Exception('Monto de stock menor a la cantidad ingresada para la venta.')

		self.__stock= self.__stock - quantity_stock

		self.__set_stock_alert()

	def add_stock(self, quantity_stock):
		if quantity_stock <= 0:
			raise Exception('Cantidad invalida de stock ingresada.')		
		
		self.__stock += quantity_stock
		
		self.__set_stock_alert()

