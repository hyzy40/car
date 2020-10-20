from unittest import TestCase

from Car import Car


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

class TestInit(TestCar):
    def test_init(self):
        self.assertEqual(self.car.time, 0)
        self.assertEqual(self.car.speed,0)
        self.assertEqual(self.car.odometer, 0)
