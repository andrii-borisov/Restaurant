import abc


class Subscriber:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, publisher, args):
        pass


class Publisher:
    def __init__(self):
        self.__changed = False
        self.subscribers = set()

    def add_subscriber(self, who):
        self.subscribers.add(who)

    def delete_subscriber(self, who):
        self.subscribers.discard(who)

    def set_changed(self):
        self.__changed = True

    def is_changed(self):
        return self.__changed

    def notify_subscribers(self, message):
        for subscriber in self.subscribers:
            subscriber.update(self, message)
