import unittest
from CPS847Midterm import Foo

class TestFooMethods(unittest.TestCase):

    def test_cps4357(self):
        foo = Foo()
        self.assertEqual(foo.cps4357(4), 16)

if __name__ == '__main__':i
    unittest.main()
