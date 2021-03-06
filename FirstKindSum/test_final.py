import time
import unittest

from FirstKindSum.fin import first_kind_sum_it_up


class MyTestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(first_kind_sum_it_up(3, 2), "1.00E+0")

    def test2(self):
        self.assertEqual(first_kind_sum_it_up(7, 6), "5.56E-3")

    def test3(self):
        self.assertEqual(first_kind_sum_it_up(9, 1), "2.83E+0")

    def test4(self):
        self.assertEqual(first_kind_sum_it_up(19, 18), "1.56E-15")

    def test5(self):
        self.assertEqual(first_kind_sum_it_up(63, 59), "3.05E-76")

    def test6(self):
        self.assertEqual(first_kind_sum_it_up(999, 999), "2.49E-2565")



if __name__ == '__main__':
    start = time.clock()
    unittest.main()
    end = time.clock()
    print "%d time passed" % end - start
