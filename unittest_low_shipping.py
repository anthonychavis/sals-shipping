import unittest
from low_shipping import find_lowest_shipping

class LowShippingTests(unittest.TestCase):
    def setUp(self) -> None:
        # return super().setUp()
        pass
    @unittest.expectedFailure
    def test_str_input(self):
        self.assertRaises(TypeError, find_lowest_shipping, 'str')
    
unittest.main()
