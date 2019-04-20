from AdvertisementStorage import AdvertisementStorage


class AdvertisementManager:
    __ad_storage = AdvertisementStorage.get_instance()

    def __init__(self, time_sec):
        self.__time_seconds = time_sec

    def process_videos(self):
        videos = self.__ad_storage.ad_list()
        videos_sets = self.__get_all_sets(videos, self.__time_seconds)

    def __get_all_sets(self, list_, time_):
        result = []
        if self.__calc_duration(list_) <= time_:
            result.append(list_)
        else:
            for i in range(len(list_)):
                new_list = list_.copy()
                del new_list[i]
                result.extend(self.__get_all_sets(new_list, time_))
        return result

    def __calc_duration(self, list_):
        duration = 0
        for item in list_:
            duration += item.get_duration()
        return duration

    def __calc_amount(self, list_):
        result = 0
        for item in list_:
            result += item.get_amount_per_one_displaying()
        return result

