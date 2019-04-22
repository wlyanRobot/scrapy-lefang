# -*- coding: utf-8 -*-
import scrapy
from ArticleSpider.items import LeFangcourseItem
from scrapy.http import Request

class LefangSpider(scrapy.Spider):
    name = 'lefang'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list/%E4%B9%90%E4%BB%BF']

    def parse(self, response):
        #课程title获取
        title =  response.xpath('//div[@class = "market-bd market-bd-6 course-list course-card-list-multi-wrap js-course-list"]\
        //li[@data-report-position]/h4/a/text()').extract()
        #课程url获取
        course_url = response.xpath(
            '//div[@class = "market-bd market-bd-6 course-list course-card-list-multi-wrap js-course-list"]\
            //li[@data-report-position]/h4/a/@href').extract()
        #课程url前加上https
        for i in range(len(course_url)):
            course_url[i-1] = 'https:'+ course_url[i-1]
        #课程提供方
        company =  response.xpath('//div[@class = "market-bd market-bd-6 course-list course-card-list-multi-wrap js-course-list"]\
        //li[@data-report-position]//span[@class="item-source"]/a/@title').extract()
        #课程价格
        price =  response.xpath('//div[@class = "market-bd market-bd-6 course-list course-card-list-multi-wrap js-course-list"]\
        //li[@data-report-position]//div[@class="item-line item-line--bottom"]/span/text()').extract()
        #购买人数
        user = response.xpath('//div[@class = "market-bd market-bd-6 course-list course-card-list-multi-wrap js-course-list"]\
        //li[@data-report-position]//div[@class="item-line item-line--middle"]/span/text()').extract()
        #购买人数数据预处理
        for i in range(0, len(user)):
            user[i] = user[i].strip()
        user = [element for element in user if len(element) >= 1]


        #爬取下一页的url
        url_nextpage =  response.xpath('//div[@class="sort-page"]//a[@class="page-next-btn icon-font i-v-right"]/@href').extract()
        #课程节数先不写，目测要重构代码，先不extract，利用对li标签可继续extract的特点，实现

        #将爬取到的数值，交给item缓存
        lefangcourseItem = LeFangcourseItem()
        lefangcourseItem["title"] = title
        lefangcourseItem["course_url"] = course_url
        lefangcourseItem["company"] = company
        lefangcourseItem["price"] = price
        lefangcourseItem["user"] = user
        yield lefangcourseItem

        if url_nextpage:
            for nextpage in url_nextpage:
                yield Request(url=nextpage, callback=self.parse)

        pass
