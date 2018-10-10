# -*- coding: utf-8 -*-
import scrapy


class ComercioelSpider(scrapy.Spider):
    name = 'comercioel'
    allowed_domains = ['elcomercio.pe']
    start_urls = ['https://elcomercio.pe/']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={"query":"discapacitados"},
            callback=self.search_list_result
        )

    #We got list for first result page
    def search_list_result(self, response):

        boxes_url = response.xpath('//h2/a/@href').extract()


        for box in boxes_url:
            boxes_url_absolute = response.urljoin(box)
            yield {
                'page_link': boxes_url_absolute
            }
        #    yield Request(boxes_url_absolute)


        #next_page = response.urljoin(response.xpath('//*[@class="next"]/a/@href').extract())
