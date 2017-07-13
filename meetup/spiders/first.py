# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import MeetupItem

class FirstSpider(CrawlSpider):
    name = 'first'
    allowed_domains = ['reddit.com']
    start_urls = ['http://www.reddit.com/r/pics/']

    rules = [
        Rule(LinkExtractor
             (allow=('/r/pics/\?count=\d*&after=\w*')),
             callback='parse_item',
             follow=True
    )
    ]

    def parse_item(self, response):

        selector_list = response.css('div.thing')

        for selector in selector_list:
            item = MeetupItem()
            item['image_urls'] = selector.xpath('a/@href').extract()
            item['title'] = selector.xpath('div/div/p/a/text()').extract()
            item['url'] = selector.xpath('a/@href').extract()

            yield item