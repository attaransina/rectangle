from unittest import TestCase
from rectangle import Rectangle


class TestRectangle(TestCase):

    def test_compute_area(self):
        rec = Rectangle(_width=10.0, _height=20.0)
        self.assertEqual(rec.compute_area(), 200.0)

    def test_correct_initialize(self):
        rec = Rectangle(_width=12.0, _height=20.0)
