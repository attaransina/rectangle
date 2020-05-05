from tests import TestShape
from shape import Rectangle


class TestRectangle(TestShape):
    shape_class = Rectangle

    def test_compute_area(self):
        rec = self.shape_class(_width=10.0, _height=20.0)
        self.assertEqual(rec.compute_area(), 200.0)

    def test_negative_width_initialize(self):
        with self.assertRaises(ValueError):
            rec = self.shape_class(_width=-1.5, _height=2.5)

    def test_negative_height_initialize(self):
        with self.assertRaises(ValueError):
            rec = self.shape_class(_width=2.0, _height=-10.5)

    def test_none_width_initialize(self):
        with self.assertRaises(TypeError):
            rec = self.shape_class(_width=None, _height=2.2)

    def test_none_height_initialize(self):
        with self.assertRaises(TypeError):
            rec = self.shape_class(_width=2.0, _height=None)

    def test_str_width_initialize(self):
        with self.assertRaises(TypeError):
            rec = self.shape_class(_width='23.0', _height=24.2)

    def test_int_with_initialize(self):
        with self.assertRaises(TypeError):
            rec = self.shape_class(_width=12, _height=12.3)

    def test_correct_initialize(self):
        rec = self.shape_class(_width=12.0, _height=20.0)
        self.assertEqual(rec.get_width(), 12.0)
        self.assertEqual(rec.get_height(), 20.0)

    def test_correct_set_height(self):
        rec = self.shape_class(_width=10.0, _height=20.0)
        self.assertEqual(rec.get_height(), 20.0)
        rec.set_height(10.0)
        self.assertEqual(rec.get_height(), 10.0)

    def test_bad_type_set_height(self):
        rec = self.shape_class(_width=10.0, _height=15.0)
        with self.assertRaises(TypeError):
            rec.set_height('25.0')

    def test_bad_value_set_width(self):
        rec = self.shape_class(_width=10.0, _height=15.0)
        with self.assertRaises(ValueError):
            rec.set_width(-1.0)

