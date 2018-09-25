#!/usr/bin/env python

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.example.com/',
    ]

    def parse(self, response):
        print(response)
        yield {
            'test':response.xpath('/html/body/div[1]/p[1]').extract(),
            'html':response.xpath('/html').extract()
        }
