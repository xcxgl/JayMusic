#!/usr/bin/Python

import scrapy

class NgaSpider(scrapy.Spider):
    name = 'NgaSpider'
    host = 'http://bbs.ngacn.cc/'
    # start_urls是准备爬取的初始页
    start_urls = ['http://bbs.ngacn.cc/thread.php?fid=406']

    # 解析函数，scrapy抓回来的页面由这个函数解析
    # 对页面的处理和分析工作都在此进行
    def parse(self, response):
        print(response.body)