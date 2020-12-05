# -*- coding: utf-8 -*-
import scrapy


class DebtsSpider(scrapy.Spider):
    name = 'debts'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        data = response.xpath("//table[@class = 'jsx-1487038798 table table-striped tp-table-body']/tbody/tr")
        for d in data:
            name = d.xpath(".//td[1]/a/text()").get() 
            link = d.xpath(".//@href").get()
            debt = d.xpath(".//td[2]/text()").get() 
            pop =  d.xpath(".//td[3]/text()").get()

            yield {
                'cname' : name,
                'clink' : link,
                'cdebt' : debt,
                'pop' : pop
            }
