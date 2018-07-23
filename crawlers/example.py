from scrapy import Spider
from scrapy import Request

class DanMasq(Spider):
    name = "danmasq"

    # https://doc.scrapy.org/en/latest/topics/settings.html
    custom_settings = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }

    def start_requests(self):
        urls = [
            'http://www.danmasq.com',
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        url = response.url
        body = response.body
        title = response.css('title::text')[0].extract()
        self.log(url)
        self.log(body)
        self.log(title)
