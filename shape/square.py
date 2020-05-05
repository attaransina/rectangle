from shape import Shape


class Square(Shape):

    def __init__(self, _sides: float):
        Shape.check_value_is_pos_number(_sides)
        self._sides = _sides

    def get_sides(self) -> float:
        return self._sides

    def set_sides(self, _sides: float):
        Shape.check_value_is_pos_number(_sides)
        self._sides = _sides

    def compute_area(self) -> float:
        return float(self._sides ** 2)
