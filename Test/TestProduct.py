import unittest, os, sys
from colour_runner.runner import ColourTextTestRunner

sys.path.insert(0, os.path.join(os.getcwd(), '../Dev/'))
from Product import *

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

if __name__ == '__main__':
	os.system('clear')
	suite = unittest.TestLoader().loadTestsFromTestCase(TestModuleProduct)
	ColourTextTestRunner(verbosity=2).run(suite)
	