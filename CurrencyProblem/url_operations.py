__version__ = "1.0.0"
__email__ = "yaninaandreaortiz@gmail.com"
__author__ = "Yanina Ortiz"

from html.parser import HTMLParser
import urllib.request


class NewHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []

    def handle_starttag(self, tag, attrs):
        """
        Find the conversion factor in a html string
        :param tag: Div tag
        :type div: str
        :param attrs: id and currency_converter_result
        :type attrs tuple
        """
        if tag == 'div':
            for name, value in attrs:
                if name == 'id' and value == 'currency_converter_result':
                    self.recording = 1

    def handle_data(self, data):
        """
        Add data to data handler
        :param data: Html parsed data
        :type data: str
        """
        if self.recording:
            self.data.append(data)

    def close(self):
        """
        Restart values
        """
        self.recording = 0
        self.data = []


class UrlOperations(object):
    def __init__(self, html_parser):
        """
        Url operations
        :param html_parser: Handler from HTMLParser
        :type html_parser: HTMLParser
        """
        self.html_parser = html_parser

    def get_conversion(self, src, dest="USD"):
        """
        Using url and currencies, return a conversion fact
        :param src: Original currency
        :type param src: str()
        :param dest: Final currenci
        :type param dest: str()
        :return: conv_factor
        :rtype: float
        """
        conv_factor = float()
        try:
            url = 'https://www.google.com/finance/converter?a=1&from={}&to={}'\
                .format(src, dest)

            response = urllib.request.urlopen(url)
            self.html_parser.feed(str(response.read()))
            convert_data = self.html_parser.data[1]
            self.html_parser.close()
            conv_factor = float(convert_data[:-4])
        except urllib.error.URLError:
            print("There was an error in url query")
            conv_factor = 0.0
        return conv_factor