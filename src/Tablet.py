
"""
Tablet
create an order and send it to the kitchen
shows ad while order is ready
"""
from kitchen.Order import Order
from ConsoleHelper import ConsoleHelper
from Observer import Publisher


class Tablet(Publisher):
    def __init__(self, number):
        Publisher.__init__(self)
        self.__number = number

    def create_order(self):
        order = Order(self)
        if not order.is_empty():
            ConsoleHelper.write_message(order)
            self.set_changed()
            self.notify_subscribers(order)
        return order

    def __str__(self):
        return 'Tablet{number=%s}' % self.__number
