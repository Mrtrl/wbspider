# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    info = scrapy.Field()


class WItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    sku_id = scrapy.Field()
    url = scrapy.Field()
    img_url = scrapy.Field()
    sold = scrapy.Field()


class GoodsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_id = scrapy.Field()
    website = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    color = scrapy.Field()
    size = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    thetype = scrapy.Field()
    brand = scrapy.Field()


class ReviewItem(scrapy.Item):
    title = scrapy.Field()
    product_id = scrapy.Field()
    website = scrapy.Field()
    score = scrapy.Field()
    content = scrapy.Field()
    size = scrapy.Field()
    time = scrapy.Field()
    review_id = scrapy.Field()

    color = scrapy.Field()
    size_ordered = scrapy.Field()
    body_type = scrapy.Field()
    body_height = scrapy.Field()
    body_weight = scrapy.Field()
    body_bust = scrapy.Field()
    body_waist = scrapy.Field()
    body_hip = scrapy.Field()
    user_name = scrapy.Field()


class PhotoItem(scrapy.Item):
    product_id = scrapy.Field()
    website = scrapy.Field()
    url = scrapy.Field()
    priority = scrapy.Field()
