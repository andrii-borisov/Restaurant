from Advertisement import Advertisement


class AdvertisementStorage:
    __instance = None
    __videos = []

    @staticmethod
    def get_instance():
        if AdvertisementStorage.__instance is None:
            AdvertisementStorage.__instance = AdvertisementStorage()
        return AdvertisementStorage.__instance

    def __init__(self):
        self.__content = object()
        self.__videos.append(Advertisement(self.__content, "First Video", 5000, 100, 3*60))
        self.__videos.append(Advertisement(self.__content, "Second Video", 100, 10, 15*60))
        self.__videos.append(Advertisement(self.__content, "Third Video", 400, 2, 10*60))

    def ad_list(self):
        return self.__videos

    def add(self, ad):
        self.__videos.append(ad)


