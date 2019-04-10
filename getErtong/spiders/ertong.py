# -*- coding: utf-8 -*-
import scrapy
from getErtong.items import GetertongItem

class ErtongSpider(scrapy.Spider):
    name = 'ertong'
    allowed_domains = ['www.qbaobei.com']
    index = 1
    startUrl = 'http://www.qbaobei.com/tag/ertongxingjiaoyu160/'
    start_urls = [startUrl + str(index) + '.html']

    def parse(self, response):
        for each in response.xpath("//ul[@class='list-conBox-ul']/li"):
            item = GetertongItem()
            item['title'] = each.xpath("./div[@class='right']/a/text()").extract()[0]
            item['content'] = each.xpath("./div[@class='right']/p/text()").extract()[0]
            item['detailUrl'] = each.xpath("./div[@class='right']/a/@href").extract()[0] 
            item['imageUrl'] = each.xpath("./a/img/@src").extract()[0] 
            yield scrapy.Request(item['detailUrl'], callback = self.parseDetail, meta={'item':item})

        self.index += 1
        url = self.startUrl + str(self.index) + '.html'
        print('xxxxxxxxxxxxxxxxxxxxx', url)
        yield scrapy.Request(url, callback=self.parse)
    
    def parseDetail(self, response):
        item = response.meta["item"]
        # print('xxxxxxxxxxxxxxxxxxxxx', item['title'])
        # print('.....................', response.xpath("//div[@class='detail-box']/p/text()").extract()[0])
        detailcontent = response.xpath("//div[@class='detail-box']/p/text()").extract()[0]
        # detailcontent = detailcontent.replace('\n', '').replace('\\r', ''), replace('\r', '')
        item['detailcontent'] = detailcontent
        yield item

