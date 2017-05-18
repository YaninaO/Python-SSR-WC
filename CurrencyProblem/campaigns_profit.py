__version__ = "1.0.0"
__email__ = "yaninaandreaortiz@gmail.com"
__author__ = "Yanina Ortiz"

from collections import Counter
import json


class CampaignsProfit(object):
    def __init__(self, url_oper, campaigns):
        """
        Operations to get profit
        :param url_oper: Url operation handler
        :type url_oper: UrlOperations
        :param campaigns: Input campaigns
        :type campaigns: dict
        """
        self.url_oper = url_oper
        self.campaigns_profit = list()
        self.campaigns = campaigns

    def calculate_revenue(self, same_campaigns):
        """
        Calculate profit por each group of campaigns
        :param same_campaigns: List of campaign with the same name
        :type same_campaigns: list()
        :return: Profit for group of campaigns
        :rtype: float
        """
        profit = 0
        for i in same_campaigns:
            int_profit = (float(i["revenue"]) - float(i["cost"])) \
                         * float(i["conversions"])
            conversion_profit = self.url_oper.get_conversion(i["currency"])\
                                * int_profit
            profit += conversion_profit
        return profit

    def set_counters(self):
        """
        Count the number of repetitions for a campaign in the starting list
        """
        self.campaigns_counters = Counter(ids["name"]
                                          for ids in self.campaigns)

    def get_profit(self):
        """
        Get profit for each group of campaign
        """
        elemens = list()
        identifier = 0
        for app in self.campaigns_counters.items():
            for counter in range(0, app[1]):
                camp_index = next(index for (index, aux_app)
                                  in enumerate(self.campaigns)
                                  if aux_app["name"] == app[0])
                elemens.append(self.campaigns[camp_index])
                self.campaigns.pop(camp_index)
            profit = self.calculate_revenue(elemens)
            self.campaigns_profit.append({"id": identifier, "name": app[0],
                                          "total_profit": profit})
            elemens = []
            identifier += 1

    def write_json_file(self):
        """
        Write Json file
        """
        with open('campaigns_data.json', 'w') as f:
            json.dump(self.campaigns_profit, f, indent=4, sort_keys=True)
        f.close()
