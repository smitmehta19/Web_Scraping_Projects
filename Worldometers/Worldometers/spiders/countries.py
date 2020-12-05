# -*- coding: utf-8 -*-
import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = [
        'www.worldometers.info']
    start_urls = [
        'http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):

        # < a href = "/world-population/china-population/" > China < /a > 
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()  # China
            # /world-population/china-population/
            link = country.xpath(".//@href").get()

            # the response which are scrapped from all the links will be sent to parse_country
            yield response.follow(url = link, callback = self.parse_country, meta = {'country_name': name})

            #absolute_url = f"https://www.worldometers.info{link}"
            # yield{
            #     'country_name': name, 
            #     'country_link': link
            # } # In scrapy if you want to return the scraped data it is always returned as a dict

    def parse_country(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath(
            "(//table[@class = 'table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            # .get() method is used to return the text as a stirng #2020
            years = row.xpath(".//td[1]/text()").get()
            pop = row.xpath(".//td[2]/strong/text()").get()  # 989866
            yield {
                'country_name' : name, 
                'curr_year': years, 
                'tot_pop': pop
            }
