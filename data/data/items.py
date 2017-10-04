# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TranscriptItem(Item):
    title = Field()
    url = Field()
    date = Field()
    company = Field()

    executives = Field()
    analysts = Field()
    body = Field()
