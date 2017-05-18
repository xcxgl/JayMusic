#!/usr/bin/Python

import scrapy

# 要建立一个Spider，你必须为scrapy.spider.BaseSpider创建一个子类，并确定三个主要的、强制的属性：
# name：爬虫的识别名，它必须是唯一的，在不同的爬虫中你必须定义不同的名字.
# start_urls：爬虫开始爬的一个URL列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些URLS开始。其他子URL将会从这些起始URL中继承性生成。
# parse()：爬虫的方法，调用时候传入从每一个URL传回的Response对象作为参数，response将会是parse方法的唯一的一个参数,
# 这个方法负责解析返回的数据、匹配抓取的数据(解析为item)并跟踪更多的URL。
class MusicSpider(scrapy.Spider):
    name = 'MusicSpider'
    # host = 'http://bbs.ngacn.cc/'
    allowed_domains = ['music.163.com']
    # start_urls是准备爬取的初始页
    start_urls = ['http://music.163.com/#/search/m/?s=%E5%91%A8%E6%9D%B0%E4%BC%A6&type=1']

    # 解析函数，scrapy抓回来的页面由这个函数解析
    # 对页面的处理和分析工作都在此进行
    def parse(self, response):
        # print(response.body)
        filename = response.url.split('/')[-1]
        open(filename, 'wb').write(response.title)

