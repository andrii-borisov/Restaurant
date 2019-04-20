from src.Observer import Subscriber
from src.ConsoleHelper import ConsoleHelper


class Waiter(Subscriber):
    def update(self, publisher, args):
        ConsoleHelper.write_message("%s was cooked by %s" % (args, publisher))

