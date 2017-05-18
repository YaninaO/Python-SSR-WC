__version__ = "1.0.0"
__email__ = "yaninaandreaortiz@gmail.com"
__author__ = "Yanina Ortiz"

from utils import InputParser
from url_operations import UrlOperations, NewHtmlParser
from campaigns_profit import CampaignsProfit


if __name__ == '__main__':
    # Url query handlres
    html_hnd = NewHtmlParser()
    url_hnd = UrlOperations(html_hnd)

    # Input file handlers
    json_file = InputParser("campaigns.json")
    js_hnd = json_file.read_json_file()

    # Campaign profit handler
    campaign_hnd = CampaignsProfit(url_hnd, js_hnd)
    campaign_hnd.set_counters()
    campaign_hnd.get_profit()
    campaign_hnd.write_json_file()
