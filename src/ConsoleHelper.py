from src.kitchen.Dish import Dish


class ConsoleHelper:
    @staticmethod
    def write_message(message):
        print message

    @staticmethod
    def read_string():
        return raw_input()

    @classmethod
    def get_all_dishes_for_order(cls):
        order = []
        cls.write_message(Dish.all_dishes_to_string())
        cls.write_message("Please enter a dish name for order or 'exit'")
        while True:
            new_order = cls.read_string()
            if new_order == 'exit':
                break
            if new_order in Dish.__members__:
                order.append(Dish[new_order])
            else:
                cls.write_message("There are no specified dish in the menu")
        return order


