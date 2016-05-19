import time
import unittest

from FirstKindSum.first_kind_sum_it_up import first_kind_sum_it_up


class MyTestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(first_kind_sum_it_up(3, 2, 4), "1.00E+0")

    def test2(self):
        self.assertEqual(first_kind_sum_it_up(7, 6, 4), "5.56E-3")

    def test3(self):
        self.assertEqual(first_kind_sum_it_up(9, 1, 4), "2.83E+0")

    def test4(self):
        self.assertEqual(first_kind_sum_it_up(19, 18, 4), "1.56E-15")

    def test5(self):
        self.assertEqual(first_kind_sum_it_up(63, 59, 4), "3.05E-76")


if __name__ == '__main__':
    start = time.clock()
    unittest.main()
    end = time.clock()
    print "%d time passed" % end - start
