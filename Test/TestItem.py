import unittest, os, sys
from colour_runner.runner import ColourTextTestRunner

sys.path.insert(0, os.path.join(os.getcwd(), '../Dev/'))
from Item import *
from Exceptions import *

class TestModuleItem(unittest.TestCase):
	def test_item_acount_init(self):

		"""
		Verify init item acount is correct.  
		"""

		item_acount = ItemAcount('Compra de Jorgito', 80.00)

		self.assertEqual(item_acount.get_item_amount(), 80.00)
		self.assertEqual(item_acount.get_description(), 'Compra de Jorgito')
		self.assertEqual(item_acount.get_quantity(), 1)
		self.assertEqual(item_acount.get_unit_price(), 80.00)

	
	def test_item_acount_init_with_invalid_amount(self):

		"""
		Verify init item acount with invalid amount.  
		"""

		self.assertRaises(InvalidAmount, ItemAcount, 'Compra de Jorgito', -80.00)


	def test_item_sale_init(self):

		"""
		Verify init item acount is correct.  
		"""

		item_sale = ItemSale('Jorgito Chcolate', 2000, 80.00, 'Jorgito', 2000, 100)

		self.assertEqual(item_sale.get_item_amount(), 160000.00)
		self.assertEqual(item_sale.get_description(), 'Jorgito Chcolate')
		self.assertEqual(item_sale.get_quantity(), 2000)
		self.assertEqual(item_sale.get_unit_price(), 80.00)
		
		self.assertEqual(item_sale.get_stock_alert(), 100)
		self.assertEqual(item_sale.get_name_product(), 'Jorgito')
		self.assertEqual(item_sale.get_stock(), 2000)
		self.assertEqual(item_sale.get_alert(), False)

	def test_item_sale_init_with_invalid_amount(self):

		"""
		Verify init item sale with invalid amount.  
		"""

		self.assertRaises(InvalidAmount, ItemSale, 'Jorgito Chcolate', -2000, 80.00, 'Jorgito', 2000, 100)
		self.assertRaises(InvalidAmount, ItemSale, 'Jorgito Chcolate', 2000, -80.00, 'Jorgito', 2000, 100)
		self.assertRaises(InvalidAmount, ItemSale, 'Jorgito Chcolate', 2000, 80.00, 'Jorgito', -2000, 100)
		self.assertRaises(InvalidAmount, ItemSale, 'Jorgito Chcolate', 2000, 80.00, 'Jorgito', 2000, -100)
		

if __name__ == '__main__':
	os.system('clear')
	suite = unittest.TestLoader().loadTestsFromTestCase(TestModuleItem)
	ColourTextTestRunner(verbosity=2).run(suite)
	