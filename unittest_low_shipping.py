import unittest

class LowShippingTests(unittest.TestCase):
    def setUp(self) -> None:
        # return super().setUp()
        pass
    @unittest.expectedFailure
    def test_str_input(self):
        raise TypeError('This test will fail')
    
unittest.main()
