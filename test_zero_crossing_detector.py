from unittest import TestCase
from ValueCrossingDetector import zero_crossing_detector, zero_crossing_detector


class TestZeroCrossingDetector(TestCase):
    def test_zero_crossing_detector1(self):
        """
        Test the most basic case of a straight line trajectory
        """
        zcd = zero_crossing_detector([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])

        self.assertEqual(zcd, 1)

    def test_zero_crossing_detector2(self):
        """
        Test the case where no crossing has occurred
        """
        zcd = zero_crossing_detector([5, 4, 3, 2, 3])

        self.assertEqual(zcd, 0)

    def test_zero_crossing_detector3(self):
        """
        Test the case where 1 crossing has occurred
        """
        zcd = zero_crossing_detector([5, 4, 3, 2, 3, -5])

        self.assertEqual(zcd, 1)

    def test_zero_crossing_detector4(self):
        """
        Test the case where 3 crossing have occurred
        """
        zcd = zero_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7])

        self.assertEqual(zcd, 3)

    def test_zero_crossing_detector4(self):
        """
        Test the case where 3 crossings have occurred but it lingers on zero (i.e. not crossing)
        """
        zcd = zero_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0])

        self.assertEqual(zcd, 3)

    def test_zero_crossing_detector5(self):
        """
        Test the case where 3 crossings have occurred, it lingers at zero and goes back (i.e. hasn't crossed)
        """
        zcd = zero_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0, -1, 0])

        self.assertEqual(zcd, 3)

    def test_zero_crossing_detector6(self):
        """
        Test the case where 3 crossings occur, it lingers at zero and then crosses
        """
        zcd = zero_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0, -1, 0, 1, 1, 1])

        self.assertEqual(zcd, 4)

    def test_zero_crossing_detector(self):
        """
        A random test
        """
        zcd = zero_crossing_detector([5, 1, 2, -3, 4, 5, 0, 0, 0, -1, 0])

        self.assertEqual(zcd, 3)


class TestValueCrossingDetector(TestCase):
    def test_value_crossing_detector1(self):
        """
        Test the most basic case of a straight line trajectory
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])

        self.assertEqual(zcd, 1)

    def test_value_crossing_detector1(self):
        """
        Test the case where no crossing has occurred
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3])

        self.assertEqual(zcd, 0)

    def test_value_crossing_detector1(self):
        """
        Test the case where 1 crossing has occurred
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5])

        self.assertEqual(zcd, 1)

    def test_value_crossing_detector1(self):
        """
        Test the case where 3 crossing have occurred
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7])

        self.assertEqual(zcd, 3)

    def test_value_crossing_detector1(self):
        """
        Test the case where 3 crossings have occurred but it lingers on zero (i.e. not crossing)
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0])

        self.assertEqual(zcd, 3)

    def test_value_crossing_detector1(self):
        """
        Test the case where 3 crossings have occurred, it lingers at zero and goes back (i.e. hasn't crossed)
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0, -1, 0])

        self.assertEqual(zcd, 3)

    def test_value_crossing_detector1(self):
        """
        Test the case where 3 crossings occur, it lingers at zero and then crosses
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0, -1, 0, 1, 1, 1])

        self.assertEqual(zcd, 4)

    def test_value_crossing_detector1(self):
        """
        A random test
        """
        zcd = value_crossing_detector([5, 1, 2, -3, 4, 5, 0, 0, 0, -1, 0])

        self.assertEqual(zcd, 3)
