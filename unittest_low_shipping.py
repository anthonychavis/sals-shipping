import unittest
from custom_exceptions import InputLengthError, NegativeWeightError
from low_shipping import find_lowest_shipping

class LowShippingTests(unittest.TestCase):
    def setUp(self) -> None:
        # return super().setUp()
        pass
    # @unittest.expectedFailure
    # def test_str_input(self):
    #     self.assertRaises(TypeError, find_lowest_shipping, 'str')
    # @unittest.expectedFailure
    # def test_neg_wt(self):
    #     self.assertRaises(NegativeWeightError, find_lowest_shipping, -9)
    @unittest.expectedFailure
    def test_len_input(self):
        self.assertRaises(InputLengthError, find_lowest_shipping, 22.10526315789)
    def test_standard_ground_expected(self):
        pass
    def test_drone_expected(self):
        pass
    def test_premium_ground_expected(self):
        pass
    def tearDown(self) -> None:
        # return super().tearDown()
        pass
    
unittest.main()
