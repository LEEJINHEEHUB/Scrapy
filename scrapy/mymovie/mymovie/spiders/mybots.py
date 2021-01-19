import scrapy
from mymovie.items import MyscraperItem
import sys

class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['movie.naver.com']
    start_urls = ['http://movie.naver.com/movie/point/af/list.nhn/']

    def parse(self, response):
        titles = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]/text()').extract()
        list_netizen_score = response.css('.st_off::text').extract()
        author = response.css('.author::text').extract()

        #zip(titles, writers, previews)
        items = []
        # items에 XPATH, CSS를 통해 추출한 데이터를 저장
        for idx in range(len(titles)):
            item = MyscraperItem()
            item['title'] = titles[idx]
            item['st_off'] = list_netizen_score[idx]
            item['author'] = author[idx]

            items.append(item)

        return items