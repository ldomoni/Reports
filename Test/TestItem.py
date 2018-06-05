import unittest, os, sys
from colour_runner.runner import ColourTextTestRunner

sys.path.insert(0, os.path.join(os.getcwd(), '../Dev/'))
from Item import *

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


if __name__ == '__main__':
	os.system('clear')
	suite = unittest.TestLoader().loadTestsFromTestCase(TestModuleItem)
	ColourTextTestRunner(verbosity=2).run(suite)
	