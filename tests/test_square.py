from tests import TestShape
from shape import Square


class TestSquare(TestShape):
    shape_class = Square

    def test_compute_area(self):
        sq = self.shape_class(_sides=10.0)
        self.assertEqual(sq.compute_area(), 100.0)

    def test_negative_sides_initialize(self):
        with self.assertRaises(ValueError):
            sq = self.shape_class(_sides=-1.5)

    def test_none_sides_initialize(self):
        with self.assertRaises(TypeError):
            sq = self.shape_class(_sides=None)

    def test_str_sides_initialize(self):
        with self.assertRaises(TypeError):
            sq = self.shape_class(_sides='23.0')

    def test_int_sides_initialize(self):
        with self.assertRaises(TypeError):
            sq = self.shape_class(_sides=12)

    def test_correct_initialize(self):
        sq = self.shape_class(_sides=12.0)
        self.assertEqual(sq.get_sides(), 12.0)

    def test_correct_set_sides(self):
        sq = self.shape_class(_sides=10.0)
        self.assertEqual(sq.get_sides(), 10.0)
        sq.set_sides(100.0)
        self.assertEqual(sq.get_sides(), 100.0)

    def test_bad_type_set_sides(self):
        sq = self.shape_class(_sides=10.0)
        with self.assertRaises(TypeError):
            sq.set_sides('25.0')

    def test_bad_value_set_width(self):
        sq = self.shape_class(_sides=10.0)
        with self.assertRaises(ValueError):
            sq.set_sides(-1.0)
