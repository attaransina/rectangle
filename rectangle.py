class Rectangle(object):

    def __init__(self, _width: float, _height: float):
        self._width = _width
        self._height = _height

    def compute_area(self):
        return float(self._width * self._height)
