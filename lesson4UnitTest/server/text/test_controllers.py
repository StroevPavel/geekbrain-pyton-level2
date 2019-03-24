import unittest

from controllers import *

class TestControllers(unittest.TestCase):

	def test_get_lower_text_is_lower(self):
		self.assertEqual(get_lower_text('TEST TEXT'), ('test text'))

	def test_get_upper_text_is_upper(self):
		self.assertEqual(get_upper_text('test text'), ('TEST TEXT'))

unittest.main()
