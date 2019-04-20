from src.ConsoleHelper import ConsoleHelper


class Order:
    def __init__(self, tablet):
        self.__dishes = ConsoleHelper.get_all_dishes_for_order()
        self.__tablet = tablet

    def __str__(self):
        if self.__dishes:
            return 'Your order: %s of %s' % (', '.join(dish.name for dish in self.__dishes), self.__tablet)
        else:
            return ''

    def get_total_cooking_time(self):
        result = 0
        for dish in self.__dishes:
            result += dish.value
        return result

    def is_empty(self):
        return True if len(self.__dishes) == 0 else False
