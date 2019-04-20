
"""
Restaurant menu
"""

from enum import Enum


class Dish(Enum):
    Fish = 25
    Steak = 30
    Soup = 15
    Juice = 5
    Water = 3

    @classmethod
    def all_dishes_to_string(cls):
        return ', '.join(dish.name for dish in Dish)

    def get_duration(self):
        return self.value
