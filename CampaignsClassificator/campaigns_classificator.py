__version__ = "1.0.0"
__email__ = "yaninaandreaortiz@gmail.com"
__author__ = "Yanina Ortiz"

from utils import InputParser
from campaigns_selector import CampaignSelector

if __name__ == '__main__':
    # Parsers initialization
    json_hnd1 = InputParser("campaigns.json")
    json_hnd2 = InputParser("user.json")
    # Read JsonFiles
    camp_data = json_hnd1.read_json_file()
    user_data = json_hnd2.read_json_file()

    # Campaign Selector initialization
    campaign_selector = CampaignSelector()
    # First filter: Platform
    platform = campaign_selector.campaigns_filter("platform",
                                                  user_data["platform"],
                                                  camp_data, all_flag=False)
    # Second filter: Gender
    gender = campaign_selector.campaigns_filter("gender", user_data["gender"],
                                                platform, all_flag=True)
    # Third filter: Connection
    connection = campaign_selector.campaigns_filter("connection",
                                                    user_data["connection"],
                                                    gender, all_flag=True)
    # Finally, age
    selected_campaing = campaign_selector.adjust_age(connection,
                                                     user_data["age"])
    if selected_campaing != {}:
        print("Selected campaign for User: {name} id: {identifier}".format(
            name=selected_campaing["name"], identifier=selected_campaing["id"]))
    else:
        print("Wow! Sadly something is wrong! We will working to get the best"
              "campaign for you.")
