import time
import unittest

from PreethiPuzzle import PreethiPuzzle


class TestPreethiPuzzle(unittest.TestCase):
    def test1v1(self):
        self.assertEqual(PreethiPuzzle("0"), 1)

    def test2v1(self):
        self.assertEqual(PreethiPuzzle("1"), 0)

    def test3v1(self):
        self.assertEqual(PreethiPuzzle("8"), 2)

    def test4v1(self):
        self.assertEqual(PreethiPuzzle("9"), 1)

    def test5v1(self):
        self.assertEqual(PreethiPuzzle("444"), 3)

    def test6v1(self):
        self.assertEqual(PreethiPuzzle("789"), 3)

    def test7v1(self):
        self.assertEqual(PreethiPuzzle("8658"), 5)


if __name__ == '__main__':
    start = time.clock()
    unittest.main()
    end = time.clock()
    print ("%d time passed" % (end - start))
