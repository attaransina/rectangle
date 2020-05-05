from unittest import TestCase
from rectangle import Rectangle


class TestRectangle(TestCase):

    def test_compute_area(self):
        rec = Rectangle(_width=10.0, _height=20.0)
        self.assertEqual(rec.compute_area(), 200.0)

    def test_correct_initialize(self):
        rec = Rectangle(_width=12.0, _height=20.0)

    def test_str_width_initialize(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(_width='23.0', _height=24.2)

    def test_int_with_initialize(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(_width=12, _height=12.3)
