# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class PacoPipeline(object):

    def __init__(self):
        self.verbindung()
        self.tabelle()

    def verbindung(self):
        self.ver = sqlite3.connect("paco.db")
        self.cur = self.ver.cursor()

    def tabelle(self):
        self.cur.execute("""drop table if exists zitate""")
        self.cur.execute("""create table zitate(
                        title text,
                        autor text)
                        """)

    def process_item(self, item, spider):
        self.speichern(item)
        return item

    def speichern(self, item):
        self.cur.execute("""insert into zitate values (?,?)""",(
            item['title'][0],
            item['autor'][0]
        ))
        self.ver.commit()
