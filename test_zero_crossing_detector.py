from unittest import TestCase
from ValueCrossingDetector import zero_crossing_detector, value_crossing_detector, zero_crossing_detector_2d,\
    value_crossing_detector_2d


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

    def test_zero_crossing_detector5(self):
        """
        Test the case where 3 crossings have occurred but it lingers on zero (i.e. not crossing)
        """
        zcd = zero_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0])

        self.assertEqual(zcd, 3)

    def test_zero_crossing_detector6(self):
        """
        Test the case where 3 crossings have occurred, it lingers at zero and goes back (i.e. hasn't crossed)
        """
        zcd = zero_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0, -1, 0])

        self.assertEqual(zcd, 3)

    def test_zero_crossing_detector7(self):
        """
        Test the case where 3 crossings occur, it lingers at zero and then crosses
        """
        zcd = zero_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0, -1, 0, 1, 1, 1])

        self.assertEqual(zcd, 4)

    def test_zero_crossing_detector8(self):
        """
        Test the most basic case of a straight line trajectory but starting with a negative
        """
        zcd = zero_crossing_detector([-5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])

        self.assertEqual(zcd, 2)

    def test_zero_crossing_detector9(self):
        """
        Test the most basic case of a straight line trajectory but starting with a zero
        """
        zcd = zero_crossing_detector([0, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])

        self.assertEqual(zcd, 1)

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
        zcd = value_crossing_detector([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5], 0)

        self.assertEqual(zcd, 1)

    def test_value_crossing_detector2(self):
        """
        Test the case where no crossing has occurred
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3], 0)

        self.assertEqual(zcd, 0)

    def test_value_crossing_detector3(self):
        """
        Test the case where 1 crossing has occurred
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5], 0)

        self.assertEqual(zcd, 1)

    def test_value_crossing_detector4(self):
        """
        Test the case where 3 crossing have occurred
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7], 0)

        self.assertEqual(zcd, 3)

    def test_value_crossing_detector5(self):
        """
        Test the case where 3 crossings have occurred but it lingers on zero (i.e. not crossing)
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0], 0)

        self.assertEqual(zcd, 3)

    def test_value_crossing_detector6(self):
        """
        Test the case where 3 crossings have occurred, it lingers at zero and goes back (i.e. hasn't crossed)
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0, -1, 0], 0)

        self.assertEqual(zcd, 3)

    def test_value_crossing_detector7(self):
        """
        Test the case where 3 crossings occur, it lingers at zero and then crosses
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0, -1, 0, 1, 1, 1], 0)

        self.assertEqual(zcd, 4)

    def test_value_crossing_detector8(self):
        """
        A random test
        """
        zcd = value_crossing_detector([5, 1, 2, -3, 4, 5, 0, 0, 0, -1, 0], 0)

        self.assertEqual(zcd, 3)

    def test_value_crossing_detector9(self):
        """
        Test the most basic case of a straight line trajectory
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5], 5)

        self.assertEqual(zcd, 0)

    def test_value_crossing_detector10(self):
        """
        Test the case where one crossing has occurred
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3], 3)

        self.assertEqual(zcd, 1)

    def test_value_crossing_detector11(self):
        """
        Test the case where 1 crossing has occurred
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5], 2)

        self.assertEqual(zcd, 1)

    def test_value_crossing_detector12(self):
        """
        Test the case where 3 crossing have occurred
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7], -1)

        self.assertEqual(zcd, 3)

    def test_value_crossing_detector13(self):
        """
        Test the case where 1 crossings have occurred but it hits the value (i.e. not crossing)
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0], 2)

        self.assertEqual(zcd, 1)

    def test_value_crossing_detector14(self):
        """
        Test the case where 2 crossings have occurred, it lingers at zero
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0, -1, 0], -6)

        self.assertEqual(zcd, 2)

    def test_value_crossing_detector15(self):
        """
        Test the case where 4 crossings occur, it lingers at zero
        """
        zcd = value_crossing_detector([5, 4, 3, 2, 3, -5, 2, -7, 0, 0, 0, -1, 0, 1, 1, 1], -1)

        self.assertEqual(zcd, 4)

    def test_value_crossing_detector16(self):
        """
        A random test
        """
        zcd = value_crossing_detector([5, 1, 2, -3, 4, 5, 0, 0, 0, -1, 0], 1)

        self.assertEqual(zcd, 3)

    def test_value_crossing_detector17(self):
        """
        A random test with non-integer value
        """
        zcd = value_crossing_detector([5, 1, 2, -3, 4, 5, 0, 0, 0, -1, 0], 0.5)

        self.assertEqual(zcd, 3)

class TestZeroCrossingDetector2D(TestCase):
    def test_zero_crossing_detector_2d1(self):
        """
        Test the most basic case of a straight line trajectory with x = 0
        """
        zcd = zero_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (0, -1), (0, -2), (0, -3),
                                         (0, -4), (0, -5)])

        self.assertEqual(zcd, 1)

    def test_zero_crossing_detector_2d2(self):
        """
        Test the case where no crossing has occurred with x = 0
        """
        zcd = zero_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 3)])

        self.assertEqual(zcd, 0)

    def test_zero_crossing_detector_2d3(self):
        """
        Test the case where 1 crossing has occurred with x = 0
        """
        zcd = zero_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 3), (0, -5)])

        self.assertEqual(zcd, 1)

    def test_zero_crossing_detector_2d4(self):
        """
        Test the case where 3 crossing have occurred with x = 0
        """
        zcd = zero_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 3), (0, -5), (0, 2), (0, -7)])

        self.assertEqual(zcd, 3)

    def test_zero_crossing_detector_2d5(self):
        """
        Test the case where 3 crossings have occurred but it lingers on zero (i.e. not crossing) with x = 0
        """
        zcd = zero_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 3), (0, -5), (0, 2), (0, -7), (0, 0),
                                         (0, 0), (0, 0)])

        self.assertEqual(zcd, 3)

    def test_zero_crossing_detector_2d6(self):
        """
        Test the case where 3 crossings have occurred, it lingers at zero and goes back (i.e. hasn't crossed) with x = 0
        """
        zcd = zero_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 3), (0, -5), (0, 2), (0, -7), (0, 0),
                                         (0, 0), (0, 0), (0, -1), (0, 0)])

        self.assertEqual(zcd, 3)

    def test_zero_crossing_detector_2d7(self):
        """
        Test the case where 3 crossings occur, it lingers at zero and then crosses with x = 0
        """
        zcd = zero_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 3), (0, -5), (0, 2), (0, -7), (0, 0),
                                         (0, 0), (0, 0), (0, -1), (0, 0), (0, 1), (0, 1), (0, 1)])

        self.assertEqual(zcd, 4)

    def test_zero_crossing_detector_2d8(self):
        """
        Test the case where 3 crossings occur, it lingers at zero and then crosses with x != 0
        """
        zcd = zero_crossing_detector_2d([(1, 5), (-1, 4), (-4, 3), (8, 2), (10, 3), (12, -5), (-45, 2), (-6, -7),
                                         (10, 0), (20, 0), (5, 0), (12, -1), (9, 0), (78, 1), (3, 1), (1, 1)])

        self.assertEqual(zcd, 4)

    def test_zero_crossing_detector_2d(self):
        """
        A random test with x = 0
        """
        zcd = zero_crossing_detector_2d([(0, 5), (0, 1), (0, 2), (0, -3), (0, 4), (0, 5), (0, 0), (0, 0), (0, 0),
                                         (0, -1), (0, 0)])

        self.assertEqual(zcd, 3)


class TestValueCrossingDetector2D(TestCase):
    def test_value_crossing_detector_2d1(self):
        """
        Test the most basic case of a straight line trajectory with x = 0
        """
        zcd = value_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (0, -1), (0, -2), (0, -3),
                                         (0, -4), (0, -5)], [(0, 0), (5, 0)])

        self.assertEqual(zcd, 1)

    def test_value_crossing_detector_2d2(self):
        """
        Test the case where no crossing has occurred with x = 0
        """
        zcd = value_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 3)], [(0, 0), (5, 0)])

        self.assertEqual(zcd, 0)

    def test_value_crossing_detector_2d3(self):
        """
        Test the case where 1 crossing has occurred with x = 0
        """
        zcd = value_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 3), (0, -5)], [(0, 0), (5, 0)])

        self.assertEqual(zcd, 1)

    def test_value_crossing_detector_2d4(self):
        """
        Test the case where 3 crossing have occurred with x = 0
        """
        zcd = value_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 3), (0, -5), (0, 2), (0, -7)],
                                         [(0, 0), (5, 0)])

        self.assertEqual(zcd, 3)

    def test_value_crossing_detector_2d5(self):
        """
        Test the case where 3 crossings have occurred but it lingers on zero (i.e. not crossing) with x = 0
        """
        zcd = value_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 3), (0, -5), (0, 2), (0, -7), (0, 0),
                                         (0, 0), (0, 0)], [(0, 0), (5, 0)])

        self.assertEqual(zcd, 3)

    def test_value_crossing_detector_2d6(self):
        """
        Test the case where 3 crossings have occurred, it lingers at zero and goes back (i.e. hasn't crossed) with x = 0
        """
        zcd = value_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 3), (0, -5), (0, 2), (0, -7), (0, 0),
                                         (0, 0), (0, 0), (0, -1), (0, 0)], [(0, 0), (5, 0)])

        self.assertEqual(zcd, 3)

    def test_value_crossing_detector_2d7(self):
        """
        Test the case where 3 crossings occur, it lingers at zero and then crosses with x = 0
        """
        zcd = value_crossing_detector_2d([(0, 5), (0, 4), (0, 3), (0, 2), (0, 3), (0, -5), (0, 2), (0, -7), (0, 0),
                                         (0, 0), (0, 0), (0, -1), (0, 0), (0, 1), (0, 1), (0, 1)], [(0, 0), (5, 0)])

        self.assertEqual(zcd, 4)

    def test_value_crossing_detector_2d8(self):
        """
        Test the case where 3 crossings occur, it lingers at zero and then crosses with x != 0
        """
        zcd = value_crossing_detector_2d([(1, 5), (-1, 4), (-4, 3), (8, 2), (10, 3), (12, -5), (-45, 2), (-6, -7),
                                         (10, 0), (20, 0), (5, 0), (12, -1), (9, 0), (78, 1), (3, 1), (1, 1)],
                                         [(0, 0), (5, 0)])

        self.assertEqual(zcd, 4)

    def test_value_crossing_detector_2d(self):
        """
        A random test with x = 0
        """
        z = [(0, 0), (1, 0), (1, -2), (2, -2), (3, -2), (3, -1), (4, -1), (5, -2), (6, -1), (6, 3), (8, 3), (10, 1),
             (7, 1),
             (3, 4)]
        a = [(0, -2), (10, 3)]

        zcd = value_crossing_detector_2d(z, a)

        self.assertEqual(zcd, 4)
