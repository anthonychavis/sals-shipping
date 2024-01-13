import unittest
from custom_exceptions import NegativeWeightError
from low_shipping import find_lowest_shipping

class LowShippingTests(unittest.TestCase):
    def setUp(self) -> None:
        # return super().setUp()
        pass
    @unittest.expectedFailure
    def test_str_input(self):
        self.assertRaises(TypeError, find_lowest_shipping, 'str')
    @unittest.expectedFailure
    def test_neg_wt(self):
        self.assertRaises(NegativeWeightError, find_lowest_shipping, -9)
    
unittest.main()
