import unittest, os, sys
from colour_runner.runner import ColourTextTestRunner

sys.path.insert(0, os.path.join(os.getcwd(), '../Dev/'))

from Product import *
from Exceptions import *

class TestModuleProduct(unittest.TestCase):
	def test_product_init(self):

		"""
		Verify init product is correct.  
		"""

		product = Product('Jorgito', 10000, 100)

		self.assertEqual(product.get_stock_alert(), 100)
		self.assertEqual(product.get_name_product(), 'Jorgito')
		self.assertEqual(product.get_stock(), 10000)
		self.assertEqual(product.get_alert(), False)


	def test_product_different(self):

		"""
		Verify that two products are different. 
		"""

		product_1 = Product('Jorgito', 10000, 100)
		product_2 = Product('Capitan del espacio', 10000, 100)
		product_3 = Product('Jorgito', 200, 10)
		
		self.assertNotEqual(product_1, product_2)
		self.assertNotEqual(product_2, product_3)
		self.assertEqual(product_1, product_3)

	def test_product_del_stock(self):

		"""
		Verify del stock to a product.
		"""

		product = Product('Jorgito', 100, 10)

		product.del_stock(30)

		self.assertEqual(product.get_stock(), 70)
		self.assertEqual(product.get_alert(), False)

	def test_product_power_on_alert_stock(self):

		"""
		Verify power on alert stock to a product.
		"""

		product = Product('Jorgito', 100, 10)

		product.del_stock(92)

		self.assertEqual(product.get_stock(), 8)
		self.assertEqual(product.get_alert(), True)

	def test_product_del_more_stock(self):

		"""
		Verify del more quantity stock to a stock product.
		"""

		product = Product('Jorgito', 100, 10)
		self.assertRaises(MenorStock, product.del_stock, 101)

	def test_product_del_invalid_quantity_stock(self):

		"""
		Verify del invalid quantity stock to a product.
		"""

		product = Product('Jorgito', 100, 10)
		self.assertRaises(InvalidAmount, product.del_stock, -10)

	def test_product_add_stock(self):

		"""
		Verify add valid stock to a product.
		"""

		product = Product('Jorgito', 100, 10)
		
		product.add_stock(30)

		self.assertEqual(product.get_stock(), 130)
		self.assertEqual(product.get_alert(), False)

	def test_product_add_invalid_stock(self):

		"""
		Verify add invalid stock to a product.
		"""

		product = Product('Jorgito', 100, 10)
		
		self.assertRaises(InvalidAmount, product.add_stock, -30)

	def test_product_power_off_alert_stock(self):

		"""
		Verify power off alert stock to a product.
		"""

		product = Product('Jorgito', 9, 10)
	
		self.assertEqual(product.get_stock(), 9)
		self.assertEqual(product.get_alert(), True)

		product.add_stock(2)

		self.assertEqual(product.get_stock(), 11)
		self.assertEqual(product.get_alert(), False)


if __name__ == '__main__':
	os.system('clear')
	suite = unittest.TestLoader().loadTestsFromTestCase(TestModuleProduct)
	ColourTextTestRunner(verbosity=2).run(suite)
	