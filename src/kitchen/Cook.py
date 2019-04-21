from src import Observer
from src.ConsoleHelper import ConsoleHelper
from src.ad.AdvertisementManager import AdvertisementManager


class Cook(Observer.Publisher, Observer.Subscriber):
    def __init__(self, name):
        super(Cook, self).__init__()
        self.__name = name

    def __str__(self):
        return self.__name

    def update(self, publisher, args):
        order = args
        ConsoleHelper.write_message('Start cooking - %s, cooking time %smin' % (order, order.get_total_cooking_time()))
        AdvertisementManager(order.get_total_cooking_time() * 60).process_videos()
        self.set_changed()
        self.notify_subscribers(args)
