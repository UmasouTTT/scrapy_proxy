# -*- coding: utf-8 -*-
import scrapy
import random
import time

from areaCode.items import CodeForAreaItem

file_path = 'path'
url_list = []
country_dict = {}
for line in open(file_path, 'r', encoding="UTF-8"):
    content = line.split(',')
    url_list.append(content[1].strip())
    country_dict[str(content[1].strip())] = content[0].strip()

class AreaCodeSpider(scrapy.Spider):
    name = "AreaCodeSpider"
    start_urls = [""]

    def __init__(self):
        self.url_count = 0

    def parse(self, response):

        print("当前url：" + response.request.url)

        yield scrapy.Request(next_url,  dont_filter=True, callback=self.parse)


    def make_requests_from_url(self, url):
        self.logger.debug('Try first time')
        return scrapy.Request(url=url, meta={'download_timeout': 3}, callback=self.parse, dont_filter=True)

