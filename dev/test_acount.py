from acount import *
import unittest, os
from colour_runner.runner import ColourTextTestRunner

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

		acount_1.add_item('Compra Lunes', 1, 10.0000)
		self.assertEqual(acount_1.get_acount_amount(), 10.0000)

		acount_1.add_item('Compra Martes', 1, 10.0000)
		self.assertEqual(acount_1.get_acount_amount(), 20.0000)

		acount_1.add_item('Pago Lunes', 1, -10.0000)
		self.assertEqual(acount_1.get_acount_amount(), 10.0000)
		
		acount_1.add_item('Pago Martes', 1, -50.0000)
		self.assertEqual(acount_1.get_acount_amount(), -40.0000)
	

	def test_journal_init(self):

		"""
		Verify init journal is correct.
		"""

		journal = Journal()

		self.assertEqual(journal.get_journal_amount(), 0.0000)	

	def test_journal_add_acount(self):

		"""
		Verify add acount in journal is correct.
		"""

		journal = Journal()
		journal.add_acount('Jorge')

		acount = journal.get_acount('Jorge')
		acount.add_item('media_luna', 1, 10.0000)
		
		self.assertEqual(journal.get_journal_amount(), 10.0000)
	
	def test_journal_acount_numbers(self):

		"""
		Verify number of acounts in journals.
		"""

		journal = Journal()

		for index in xrange(1, 20):
			acount = Acount('luz_%s' %index)
			journal.add_acount(acount)

			self.assertEqual(journal.get_number_acounts(), index)

if __name__ == '__main__':
	os.system('clear')
	suite = unittest.TestLoader().loadTestsFromTestCase(TestModuleAcount)
	ColourTextTestRunner(verbosity=2).run(suite)
	