__version__ = "1.0.0"
__email__ = "yaninaandreaortiz@gmail.com"
__author__ = "Yanina Ortiz"

from collections import Counter
from html.parser import HTMLParser
import urllib.request
import json
from utils import InputParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []

    def handle_starttag(self, tag, attrs):
         if tag == 'div':
            for name, value in attrs:
                if name == 'id' and value == 'currency_converter_result':
                    self.recording = 1

    def handle_data(self, data):
        if self.recording:
            self.data.append(data)

    def close(self):
        self.recording = 0
        self.data = []


class UrlOperations(object):
    def __init__(self, html_parser):
        self.html_parser = html_parser

    def get_conversion(self, src, dest="USD"):
        url = 'https://www.google.com/finance/converter?a=1&from={}&to={}'.format(src, dest)
        response = urllib.request.urlopen(url)
        self.html_parser.feed(str(response.read()))
        convert_data = self.html_parser.data[1]
        self.html_parser.close()
        return float(convert_data[:-4])


class CampaignsProfit(object):
    def __init__(self, url_oper, campaigns):
        self.url_oper = url_oper
        self.campaigns_profit = list()
        self.campaigns = campaigns

    def calculate_revenue(self, lista):
        profit = 0
        for i in lista:
            int_profit = (float(i["revenue"]) - float(i["cost"])) * float(i["conversions"])
            conversion_factor = self.url_oper.get_conversion(i["currency"]) * int_profit
            profit += conversion_factor
        return profit

    def set_counters(self):
        self.campaigns_counters = Counter(ids["name"] for ids in self.campaigns)
        print(self.campaigns_counters)

    def get_profit(self):
        elemens = list()
        identifier = 0
        for app in self.campaigns_counters.items():
            for counter in range(0, app[1]):
                camp_index = next(index for (index, aux_app) in enumerate(self.campaigns)
                                  if aux_app["name"] == app[0])
                elemens.append(self.campaigns[camp_index])
                self.campaigns.pop(camp_index)
            profit = self.calculate_revenue(elemens)
            self.campaigns_profit.append({"id": identifier, "name": app[0], "total_profit": profit})
            print(app)
            print(identifier)
            elemens = []
            identifier += 1

    def write_json_file(self):
        with open('campaigns_data.json', 'w') as f:
            json.dump(self.campaigns_profit, f, indent=4, sort_keys=True)
        f.close()


if __name__ == '__main__':
    html_hnd = MyHTMLParser()
    url_hnd = UrlOperations(html_hnd)
    json_file = InputParser("campaigns.json")
    js_hnd = json_file.read_json_file()
    campaign_hnd = CampaignsProfit(url_hnd, js_hnd)
    campaign_hnd.set_counters()
    campaign_hnd.get_profit()
    campaign_hnd.write_json_file()
