# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class GetertongPipeline(object):
    def process_item(self, item, spider):
        # db = pymysql.connect('localhost', 'root', '897011805', 'yhj')
        # cursor = db.cursor()
        title = pymysql.escape_string(item['title'])
        detailUrl = pymysql.escape_string(item['detailUrl'])
        content = pymysql.escape_string(item['content'])
        imageUrl = pymysql.escape_string(item['imageUrl'])
        detailcontent = pymysql.escape_string(item['detailcontent'])
        sql = '''INSERT INTO ertong VALUES ('%s', '%s', '%s', '%s, '%s)'''%(title, detailUrl, content, imageUrl, detailcontent)
        # cursor.execute(sql)
        # db.commit()
        # db.close()
        print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,', sql)
        return item
