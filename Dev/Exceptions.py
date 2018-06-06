class DevExceptions(Exception):
	def __init__(self, message):
	    self.__message = message

	def get_message(self):
		return self.__message

class MenorStock(DevExceptions):
	def __init__(self, message):
		super(MenorStock, self).__init__(message)


class InvalidAmount(DevExceptions):
	def __init__(self, message):
		super(InvalidAmount, self).__init__(message)
	