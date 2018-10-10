# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class ComercioelSpider(Spider):
    name = 'comercioel'
    allowed_domains = ['elcomercio.pe']
    #start_urls = ['https://elcomercio.pe/']
    start_urls = ['https://elcomercio.pe/buscar/?query=discapacitados']


    def parse(self, response):
        #return scrapy.FormRequest.from_response(
        #    response,
        #    formdata={"query":"discapacitados"},
        #    callback=self.search_list_result
        #)
        boxes_url = response.xpath('//h2/a/@href').extract()

        for box in boxes_url:
            boxes_url_absolute = response.urljoin(box)
            yield {
                'page_link': boxes_url_absolute
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        self.logger.info("------------------------- %s",next_page_url)
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    #We got list for first result page
    def search_list_result(self, response):

        boxes_url = response.xpath('//h2/a/@href').extract()

        for box in boxes_url:
            boxes_url_absolute = response.urljoin(box)
            yield {
                'page_link': boxes_url_absolute
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        self.logger.info("------------------------- %s",next_page_url)
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

        #next_page = response.urljoin(response.xpath('//*[@class="next"]/a/@href').extract())
