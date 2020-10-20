from unittest import TestCase

from car.Car import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car()


class TestBrake(TestCar):
    def test_brake(self):
        self.car.brake()

        self.assertEqual(self.car.speed, 0)

    def test_accelerate_brake(self):
        self.car.accelerate()

        self.assertEqual(self.car.speed, 5)

        self.car.brake()

        self.assertEqual(self.car.speed, 0)

