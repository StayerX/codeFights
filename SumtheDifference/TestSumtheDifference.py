import time
import unittest

from SumtheDifference import SumtheDifferenceV1, SumtheDifferenceV2


class MyTestCase1(unittest.TestCase):
    def test1v1(self):
        self.assertEqual(SumtheDifferenceV1("(-100) + 100  - (-200) + 1"), -3)

    def test2v1(self):
        self.assertEqual(SumtheDifferenceV1("(-25) + (-75) + 50 - 40 - (22 + 2)"), -8)

    def test3v1(self):
        self.assertEqual(SumtheDifferenceV1("999 + 999 + 999 + 888 + 888 - (-777)"), -40)

    def test4v1(self):
        self.assertEqual(SumtheDifferenceV1("(-25) + (-75 )+ 50 - (-40 ) - (-80)"), -22)

    def test5v1(self):
        self.assertEqual(SumtheDifferenceV1("(2-262+(+))7182(++1 "), 9)

    def test6v1(self):
        self.assertEqual(SumtheDifferenceV1("(2-262+(+))7182(++1 "), 9)

    def test7v1(self):
        self.assertEqual(SumtheDifferenceV1("49)-3044203+571+7335 "), -26)

    def test8v1(self):
        self.assertEqual(SumtheDifferenceV1(""), 0)


class MyTestCase2(unittest.TestCase):
    def test1v2(self):
        self.assertEqual(SumtheDifferenceV1("2 + -)     2        "), 4)

    def test1v2(self):
        self.assertEqual(SumtheDifferenceV2("(-100) + 100  - (-200) + 1"), -3)

    def test2v2(self):
        self.assertEqual(SumtheDifferenceV2("(-25) + (-75) + 50 - 40 - (22 + 2)"), -8)

    def test3v2(self):
        self.assertEqual(SumtheDifferenceV2("999 + 999 + 999 + 888 + 888 - (-777)"), -40)

    def test4v2(self):
        self.assertEqual(SumtheDifferenceV2("(-25) + (-75 )+ 50 - (-40 ) - (-80)"), -22)

    def test5v2(self):
        self.assertEqual(SumtheDifferenceV2("(2-262+(+))7182(++1 "), 9)

    def test6v2(self):
        self.assertEqual(SumtheDifferenceV2("(2-262+(+))7182(++1 "), 9)

    def test7v2(self):
        self.assertEqual(SumtheDifferenceV2("49)-3044203+571+7335 "), -26)

    def test8v2(self):
        self.assertEqual(SumtheDifferenceV2(""), 0)

    def test1v2(self):
        self.assertEqual(SumtheDifferenceV2("2 + -)     2        "), 4)


if __name__ == '__main__':
    start = time.clock()
    unittest.main()
    end = time.clock()
    print "%d time passed" % end - start
`