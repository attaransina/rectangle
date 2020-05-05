from unittest import TestCase
from rectangle import Rectangle


class TestRectangle(TestCase):

    def test_compute_area(self):
        rec = Rectangle(_width=10.0, _height=20.0)
        self.assertEqual(rec.compute_area(), 200.0)

    def test_correct_initialize(self):
        rec = Rectangle(_width=12.0, _height=20.0)

    def test_negative_width_initialize(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(_width=-1.5, _height=2.5)

    def test_negative_height_initialize(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(_width=2.0, _height=-10.5)

    def test_none_width_initialize(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(_width=None, _height=2.2)

    def test_none_height_initialize(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(_width=2.0, _height=None)
