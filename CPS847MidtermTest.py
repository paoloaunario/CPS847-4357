import unittest
from CPS847Midterm import Foo

class TestMethods(unittest.TestCase):

    def cps4357(self):
        foo = Foo()
        self.assertEqual(foo.cps4357(4), 16)

if __name__ == '__main__':
    unittest.main()
