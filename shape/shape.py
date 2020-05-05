from abc import ABC, abstractmethod


class Shape(ABC):

    @staticmethod
    def check_value_is_pos_number(value):
        if value is None:
            raise TypeError('value should not be None')
        if not isinstance(value, float):
            raise TypeError('value should be float')
        if value <= 0:
            raise ValueError('value should be greater than zero')

    @abstractmethod
    def compute_area(self) -> float:
        raise NotImplementedError
