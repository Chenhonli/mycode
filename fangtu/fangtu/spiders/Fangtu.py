# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class FangtuSpider(scrapy.Spider):
    name = 'Fangtu'
    allowed_domains = ['http://www.tuniu.com']
    start_urls = ['http://http://www.tuniu.com/']

    def parse(self, response):
        pass
