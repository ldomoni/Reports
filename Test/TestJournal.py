from colour_runner.runner import ColourTextTestRunner
import unittest, os, sys

sys.path.insert(0, os.path.join(os.getcwd(), '../Dev/'))
from Journal import *

class TestModuleAcount(unittest.TestCase):
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
	