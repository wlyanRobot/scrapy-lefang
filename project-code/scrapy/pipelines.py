# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class LeFangcoursePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="wlyan_Robot", db="scrapyspider", charset="utf8")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        for j in range(0, len(item["title"])):
            if item["company"][j] == '乐仿':
                title = item["title"][j]
                course_url = item["course_url"][j]
                company = item["company"][j]
                price = item["price"][j]
                user = item["user"][j]
                insert_sql = """
                    insert into lefangcourse(title, user, price, course_url, company)
                    VALUES (%s, %s, %s, %s, %s)
                """
                self.cursor.execute(insert_sql, (title, user, price, course_url, company))
                self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()

