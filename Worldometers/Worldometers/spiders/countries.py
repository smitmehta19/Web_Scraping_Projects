# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = [
        'www.worldometers.info/world-population/population-by-country']
    start_urls = [
        'http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        title = response.xpath("//h1/text()").get()
        countries = response.xpath("//td/a/text()").getall()

# In scrapy if you want to return the scraped data it is always returned as a dict
        yield{
            'title': title,
            'countries': countries
        }
