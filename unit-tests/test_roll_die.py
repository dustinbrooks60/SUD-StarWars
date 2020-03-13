from unittest import TestCase
from character import roll_die
import random


class TestRoll_die(TestCase):
    def test_equal_zero_roll_die(self):
        self.assertEqual(roll_die(0, 6), 0)

    def test_equal_zero_2_roll_die(self):
        self.assertEqual(roll_die(3, 0), 0)

    def test_both_equal_zero_roll_die(self):
        self.assertEqual(roll_die(0, 0), 0)

    def test_below_zero_roll_die(self):
        self.assertEqual(roll_die(-1, 3), 0)

    def test_below_zero_2_roll_die(self):
        self.assertEqual(roll_die(3, -1), 0)

    def test_predetermined_roll_die(self):
        random.seed(1)
        self.assertEqual(roll_die(1, 6), 2)
        random.seed()

    def test_predetermined_2_roll_die(self):
        random.seed(1)
        self.assertEqual(roll_die(1, 8), 3)
        random.seed()

    def test_predetermined_3_roll_die(self):
        random.seed(4)
        self.assertEqual(roll_die(1, 10), 4)
        random.seed()

    def test_predetermined_4_roll_die(self):
        random.seed(10)
        self.assertEqual(roll_die(1, 12), 10)
        random.seed()

    def test_predetermined_5_roll_die(self):
        random.seed(42)
        self.assertEqual(roll_die(1, 12), 11)
        random.seed()

    def test_predetermined_6_roll_die(self):
        random.seed(15)
        self.assertEqual(roll_die(2, 6), 5)
        random.seed()

    def test_predetermined_7_roll_die(self):
        random.seed(24)
        self.assertEqual(roll_die(3, 6), 15)
        random.seed()

