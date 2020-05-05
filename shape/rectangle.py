from .shape import Shape


class Rectangle(Shape):

    def __init__(self, _width: float, _height: float):
        Rectangle.check_value_is_pos_number(_width)
        Rectangle.check_value_is_pos_number(_height)
        self._width = _width
        self._height = _height

    def compute_area(self):
        return float(self._width * self._height)

    def get_width(self) -> float:
        return self._width

    def set_width(self, _width: float):
        Rectangle.check_value_is_pos_number(_width)
        self._width = _width

    def get_height(self) -> float:
        return self._height

    def set_height(self, _height: float):
        Rectangle.check_value_is_pos_number(_height)
        self._height = _height
