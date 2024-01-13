import unittest

class LowShippingTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_str_input(self):
        raise TypeError('This test will fail')
    
unittest.main()
