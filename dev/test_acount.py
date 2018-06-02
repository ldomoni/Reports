from acount import *
import unittest, os
from colour_runner.runner import ColourTextTestRunner

class TestModuleAcount(unittest.TestCase):
	def test_acount_init(self):

		"""
		Verify init acount is correct.  
		"""

		acount_1 = Acount('luz')

		self.assertEqual(acount_1.get_acount_amount(), 0.0000)
		self.assertEqual(acount_1.get_name_acount(), 'luz')

	def test_acount_name(self):

		"""
		Verify that two acounts are different. 
		"""

		acount_luz_1 = Acount('luz_1')
		acount_luz_2 = Acount('luz_2')

		self.assertNotEqual(acount_luz_1.get_name_acount(), acount_luz_2.get_name_acount())

	def test_acount_add_item(self):

		"""
		Verify add item in acount are correct. 
		"""

		acount_1 = Acount('Panaderia')

		acount_1.add_item('media_luna', 1, 10.0000)
		self.assertEqual(acount_1.get_acount_amount(), 10.0000)

		acount_1.add_item('media_luna', 1, 10.00001)
		self.assertEqual(acount_1.get_acount_amount(), 20.00001)

		acount_1.add_item('media_luna', 1, 10.00009)
		self.assertEqual(acount_1.get_acount_amount(), 30.0001)
		
		acount_1.add_item('media_luna', 1, 10.00004)
		self.assertEqual(acount_1.get_acount_amount(), 40.00014)
	
	def test_acount_cancel_item(self):

		"""
		Verify cancel items in acount are correct. 
		"""

		acount_1 = Acount('luz')

		acount_1.add_item('media_luna', 10, 10.0000)

		acount_1.cancel_item('media_luna', 1, 10.0000)
		self.assertEqual(acount_1.get_acount_amount(),90.0000)

		acount_1.cancel_item('media_luna', 2, 10.0000)
		self.assertEqual(acount_1.get_acount_amount(), 70.0000)
			
		acount_1.cancel_item('media_luna', 3, 10.0000)
		self.assertEqual(acount_1.get_acount_amount(), 40.0000)

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
		journal.add_acount('luz')

		acount = journal.get_acount('luz')
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
	