import unittest, os, sys
from colour_runner.runner import ColourTextTestRunner

sys.path.insert(0, os.path.join(os.getcwd(), '../Dev/'))
from Acount import *

class TestModuleAcount(unittest.TestCase):
	def test_acount_init(self):

		"""
		Verify init acount is correct.  
		"""

		acount_1 = Acount('Jorge')

		self.assertEqual(acount_1.get_acount_amount(), 0.0000)
		self.assertEqual(acount_1.get_name_acount(), 'Jorge')

	def test_acount_name(self):

		"""
		Verify that two acounts are different. 
		"""

		acount_luz_1 = Acount('Jorge')
		acount_luz_2 = Acount('Gaston')

		self.assertNotEqual(acount_luz_1.get_name_acount(), acount_luz_2.get_name_acount())

	def test_acount_add_item(self):

		"""
		Verify add item in acount are correct. 
		"""

		acount_1 = Acount('Jorge')

		acount_1.add_item('Compra Lunes', 10.0000)
		self.assertEqual(acount_1.get_acount_amount(), 10.0000)

		acount_1.add_item('Compra Martes', 10.0000)
		self.assertEqual(acount_1.get_acount_amount(), 20.0000)

		acount_1.add_item('Pago Lunes', -10.0000)
		self.assertEqual(acount_1.get_acount_amount(), 10.0000)
		
		acount_1.add_item('Pago Martes', -50.0000)
		self.assertEqual(acount_1.get_acount_amount(), -40.0000)
	


if __name__ == '__main__':
	os.system('clear')
	suite = unittest.TestLoader().loadTestsFromTestCase(TestModuleAcount)
	ColourTextTestRunner(verbosity=2).run(suite)
	