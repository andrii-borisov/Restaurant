
class Advertisement:
    def __init__(self, content, name, initial_amount, hits, duration):
        self.__content = content
        self.__name = name
        self.__initial_amount = initial_amount
        self.__hits = hits
        self.__duration = duration
        self.__amount_per_one_displaying = 0 if self.__hits == 0 else (self.__initial_amount/self.__hits)

    def get_name(self):
        return self.__name

    def get_duration(self):
        return self.__duration

    def get_amount_per_one_displaying(self):
        return self.__amount_per_one_displaying if self.__hits > 0 else 0

    def revalidate(self):
        if self.__hits <= 0:
            raise AttributeError
        self.__hits -= 1

    def __str__(self):
        return "Advertisement{name='%s', duration=%s}" % (self.__name, self.__duration)


