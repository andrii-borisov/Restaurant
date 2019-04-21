from AdvertisementStorage import AdvertisementStorage
from src.ConsoleHelper import ConsoleHelper


class AdvertisementManager:
    __ad_storage = AdvertisementStorage.get_instance()

    def __init__(self, time_sec):
        self.__time_seconds = time_sec

    def process_videos(self):
        videos = self.__ad_storage.ad_list()
        videos_sets = self.__get_all_sets(videos, self.__time_seconds)
        result_list = self.__get_best_set(videos_sets)
        for ad in result_list:
            self.__print_ad(ad)
            ad.revalidate()

    def __get_all_sets(self, list_, time_):
        result = []
        if self.__calc_duration_of_list(list_) <= time_:
            result.append(list_)
        else:
            for i in range(len(list_)):
                new_list = list_[:]
                del new_list[i]
                result.extend(self.__get_all_sets(new_list, time_))
        return result

    def __calc_duration_of_list(self, list_):
        duration = 0
        for item in list_:
            duration += item.get_duration()
        return duration

    def __calc_amount_of_list(self, list_):
        result = 0
        for item in list_:
            result += item.get_amount_per_one_displaying()
        return result

    def __get_best_set(self, list_of_sets):
        if len(list_of_sets) == 1:
            return list_of_sets[0]
        result = []
        max_amount = self.__calc_amount_of_list(list_of_sets[0])
        for candidate_list in list_of_sets:
            clear_list = self.__validate_list(candidate_list)
            amount = self.__calc_amount_of_list(clear_list)
            if max_amount < amount:
                result = clear_list
        return result

    def __validate_list(self, list_of_videos):
        """
        Remove ad with zero amount (end of video showing) from the list.
        @:param raw list of the videos
        @:return list of the videos for showing
        """
        return [ad for ad in list_of_videos if ad.get_amount_per_one_displaying() != 0]

    def __print_ad(self, ad):
        ConsoleHelper.write_message("%s is displaying... %s, %s" % (ad.get_name(), ad.get_amount_per_one_displaying(), int(ad.get_amount_per_one_displaying()/float(ad.get_duration())*1000)))


