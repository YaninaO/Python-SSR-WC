__version__ = "1.0.0"
__email__ = "yaninaandreaortiz@gmail.com"
__author__ = "Yanina Ortiz"


class CampaignSelector(object):
    def __init__(self):
        pass

    def campaigns_filter(self, key, expected_value,
                         campaigns_lists, all_flag=False):
        """
        Returns list of campaigns which better adjust with expected_value
        :param all_flag: Aplies filter to All key
        :type all_flag: bool
        :param key: Key to be founded in the campaigns_lists
        :type key: str
        :param campaigns_lists: List whose contains a different campaigns
        :type campaigns_lists: list(dict)
        :param expected_value: Expected value to be founded in campaigns list
        :type expected_value: str
        :return: The matched campaings list
        :rtype: list(dict)
        """
        if all_flag:
            filter_campaigns = \
                list(filter(lambda aux_value: aux_value[key] == expected_value,
                       campaigns_lists)) + \
                list(filter(lambda aux_value: aux_value[key] == "All",
                       campaigns_lists))
        else:
            filter_campaigns = \
                list(filter(lambda aux_value: aux_value[key] == expected_value,
                            campaigns_lists))

        if filter_campaigns == [] and all_flag == False:
            filter_campaigns = self.campaigns_filter(key, expected_value,
                                                     campaigns_lists, all_flag=True)
        else:
            pass

        return filter_campaigns

    def filter_age(self, min_age, max_age, user_age):
        """
        Return True if the user is allowed to use campaing.
        False otherwise
        :param min_age: Min age allowed to use the campaign
        :type min_age: int
        :param max_age: Max age allowed to use the campaign
        :type max_age: int
        :param user_age: The user age
        :type user_age: str
        :return : True in accepted_age if user age belongs a
        at the age range of the campaign and an average number
        considering the age limits and age of the user
        :rtype: tuple(int, bool)
        """

        accepted_age = True
        min_restr = True
        max_restr = True
        result = 0
        null_max = 110
        null_min = 0

        if min_age is None:
            min_restr = False
        if max_age is None:
            max_restr = False

        if max_restr and min_restr:
            accepted_age = min_age <= int(user_age) <= max_age
            result = abs(((max_age - min_age)/2 + min_age) - int(user_age))
        elif not (max_restr or min_restr):
            accepted_age = True
            result = abs(((null_max - null_min)/2 + null_min) - int(user_age))
        elif max_restr:
            accepted_age = int(user_age) <= max_age
            result = abs(((max_age - null_min)/2 + null_min) - int(user_age))
        elif min_restr:
            accepted_age = min_age <= int(user_age)
            result = abs(((null_max - min_age)/2 + min_age) - int(user_age))

        return result, accepted_age

    def adjust_age(self, campaigns, user_age):
        """
        Select best campaing according age limits
        :param campaigns: Campaigns
        :type campaigns: list()
        :param user_age: User age
        :type user_age: str
        :return: Selected campaing
        :rtype: dict()
        """
        selected_camp = dict()
        previous_result = 1000
        for camp in campaigns:
            result, accept = self.filter_age(camp["min_age"],
                                             camp["max_age"], user_age)
            if accept and result <= previous_result:
                selected_camp = camp
            previous_result = result
        return selected_camp
