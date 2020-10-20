from unittest import TestCase

from Car import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car()


class TestInit(TestCar):
    def test_init(self):
        self.assertEqual(self.car.time, 0)
        self.assertEqual(self.car.speed,0)
        self.assertEqual(self.car.odometer, 0)