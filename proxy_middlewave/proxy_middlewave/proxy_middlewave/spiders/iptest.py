import scrapy
import scrapy.http.response as response
from scrapy.http import Request, Response
from items import ProxyMiddlewaveItem


class IPSpider(scrapy.Spider):
    name = 'IPSpider'
    start_urls = [
        'http://exercise.kingname.info/exercise_middleware_ip/1'
    ]
    page = 1
    limit = 2

    def parse(self, response):
        """回调函数处理response"""
        selector = response.selector
        # 生成item对象
        # print(response.text)
        proxy_item = ProxyMiddlewaveItem()
        proxy_item['ip'] = response.selector.xpath('//body/p/text()').get()
        yield proxy_item
        # 生成Request对象
        self.page += 1
        if self.page < self.limit:
            yield Request(url='http://exercise.kingname.info/exercise_middleware_ip/{}'.format(self.page))
        else:
            print('结束抓取')
