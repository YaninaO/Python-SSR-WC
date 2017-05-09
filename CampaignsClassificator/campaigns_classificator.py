# Campaigns classificator file.

# author = yortiz

import json


def read_json_file(path_file):
    """
    Parse a JSON file
    :param path_file: Path to json file
    :type path_file: str
    :return: Parsed file
    :rtype: list(dict)
    """
    with open(path_file) as camp_json:
        camp_data = json.load(camp_json)
    return camp_data


def campaigns_filter(key, expected_value, campaigns_lists):
    """
    Returns list of campaigns which better adjust with expected_value
    :param key: Key to be founded in the campaigns_lists
    :type key: str
    :param campaigns_lists: List whose contains a different campaigns
    :type campaigns_lists: list(dict)
    :param expected_value: Expected value to be founded in campaigns list
    :type expected_value: str
    :return: The matched campaings list
    :rtype: list(dict)
    """
    filter_campaigns = \
        filter(lambda aux_value: aux_value[key] == expected_value,
               campaigns_lists)
    return list(filter_campaigns)


def age_filter(min_age, max_age, user_age):
    """
    Return True if the user is allowed to use some campaing. False otherwise
    :param min_age: Min age allowed to use the campaign
    :type min_age: int
    :param max_age: Max age allowed to use the campaign
    :type max_age: int
    :param user_age: The user age
    :type user_age: int
    :return: 
    :rtype: Bool
    """

    accepted_age = True
    min_restr = True
    max_restr = True

    if min_age is None:
        min_restr = False
    if max_age is None:
        max_restr = False

    if max_restr and min_restr:
        accepted_age = min_age <= int(user_age) <= max_age
    elif not (max_restr or min_restr):
        accepted_age = True
    elif max_restr:
        accepted_age = int(user_age) <= max_age
    elif min_restr:
        accepted_age = min_age <= int(user_age)

    return accepted_age


if __name__ == '__main__':
    camp_data = read_json_file("campaigns.json")
    user_data = read_json_file("user.json")
    platform = campaigns_filter("platform", user_data["platform"], camp_data)
    gender = campaigns_filter("gender", user_data["gender"], platform) \
             + campaigns_filter("gender", "All", platform)
    connection = campaigns_filter("connection", user_data["connection"], gender) \
                 + campaigns_filter("connection", "All", gender)
    selected_campaign = list(filter(lambda age: age_filter(age["min_age"],
                                                           age["max_age"],
                                                           user_data["age"])
                                                == True, connection))

    print(selected_campaign)
