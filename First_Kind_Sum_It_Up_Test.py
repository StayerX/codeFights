import unittest, time
import First_Kind_Sum_It_Up.py


class MyTestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(First_Kind_Sum_It_Up(3,2), "1.00E+0")

    def test2(self):
        self.assertEqual(First_Kind_Sum_It_Up(7,6), "5.56E-3")

    def test3(self):
        self.assertEqual(First_Kind_Sum_It_Up(9,1), "2.83E+0")

    def test4(self):
        self.assertEqual(First_Kind_Sum_It_Up(19, 18), "1.56E-15")

    def test5(self):
        self.assertEqual(First_Kind_Sum_It_Up(63, 59), "3.05E-76")

if __name__ == '__main__':
    start = time.clock()
    unittest.main()
    end = time.clock()
    print "%d time passed" % end - start
