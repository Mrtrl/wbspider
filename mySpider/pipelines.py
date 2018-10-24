# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import logging
from mySpider.items import WItem
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

logger = logging.getLogger('SaveImagePipeline')


class GenPipeline(object):
    def open_spider(self, spider):
        path = os.path.dirname(os.path.realpath(__file__))
        self.file = os.open(path + '/json_file/{}.json'.format(spider.name), os.O_RDWR | os.O_CREAT)
        self.log = open(path + '/log/{}.json'.format(spider.name), 'wb')
        self.file_size = 0

    def process_item(self, item, spider):
        if isinstance(item, WItem):
            item_str = json.dumps(dict(item)) + '\n'
            self.file_size += os.write(self.file, item_str)

        # elif isinstance(item, PhotoItem):
        #     item_str = json.dumps(dict(item)) + '\n'
        #     self.file_size += os.write(self.file, item_str)

        # elif isinstance(item, ReviewItem):
        #     item_str = json.dumps(dict(item)) + '\n'
        #     self.file_size += os.write(self.file, item_str)

        return item

    def close_spider(self, spider):
        log_dict = {}
        log_dict['spider'] = spider.name
        log_dict['file_size'] = self.file_size

        log_str = json.dumps(log_dict)
        self.log.write(log_str)

        os.close(self.file)
        self.log.close()


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 此方法获取的是requests 所以用yield 不要return
        yield scrapy.Request(url=item['img_url'])

    def item_completed(self, results, item, info):
        """
        文件下载完成之后，返回一个列表 results
        列表中是一个元组，第一个值是布尔值，请求成功会失败，第二个值的下载到的资源
        """
        if not results[0][0]:
            # 如果下载失败，就抛出异常，并丢弃这个item
            # 被丢弃的item将不会被之后的pipeline组件所处理
            raise DropItem('下载失败')
        # 打印日志
        logger.debug('下载图片成功')
        return item

    def file_path(self, request, response=None, info=None):
        """
        返回文件名
        """
        return request.url.split('/')[-1]
