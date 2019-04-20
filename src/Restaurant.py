import Tablet
import kitchen.Cook as Cook
import kitchen.Waiter as Waiter

"""
Restaurant application
"""


class Restaurant:
    def __init__(self, table_number, cooker_name):
        self.__tablet = Tablet.Tablet(table_number)
        self.__cooker = Cook.Cook(cooker_name)
        self.__tablet.add_subscriber(self.__cooker)
        self.__waiter = Waiter.Waiter()
        self.__cooker.add_subscriber(self.__waiter)
        self.__tablet.create_order()


if __name__ == '__main__':
    Restaurant(8, 'Gordon James Ramsay Jr')
