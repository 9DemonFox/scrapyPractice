# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import re


class ProxyMiddlewavePipeline(object):
    def process_item(self, item, spider):
        return item


class addHttp(object):
    '''
    添加http://头
    '''

    def process_item(self, item, spider):
        if item.get('ip'):
            item['ip'] = re.sub('你在第[\d]+页，你的IP为: ', '', item.get('ip'))
            return item
        else:
            raise DropItem('Item不存在,丢弃')


class save2csv(object):
    '''
    写入文件
    '''

    # 启动spider时打开
    def open_spider(self, spider):
        self.file = open('items.csv', 'w+')

    # 关闭spider时打开
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        ip = item.get('ip')
        if ip:
            self.file.writelines(ip)
            return item
        else:
            raise DropItem('Item不存在,丢弃')
