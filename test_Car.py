from unittest import TestCase

from Car import Car

class TestCar(TestCase):
    def setUp(self):
        self.car=Car()

class TestStep(TestCar):
    def test_step(self):
        self.assertEqual(self.car.time, 0)
        self.car.step()
        self.assertEqual(self.car.time, 1)

    def test_odometer(self):
        self.assertEqual(self.car.odometer,0)
        self.car.accelerate()
        self.car.step()
        self.assertEqual(self.car.odometer,5)

