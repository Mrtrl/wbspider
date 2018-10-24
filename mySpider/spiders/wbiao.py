# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import WItem
import re


class WbiaoSpider(scrapy.Spider):
    name = 'wbiao'
    allowed_domains = ['wbiao.cn']
    start_urls = ['https://www.wbiao.cn/shoubiao.html']

    def parse(self, response):
        # create item
        goods_item = WItem()

        # judge if has data
        if response.xpath(r'//div[@class="no_srh_result"]'):
            return

        # sku_parse
        sku_list = response.xpath(r'//div[@class="s_goods_list"]/ul/li')
        for sku in sku_list:
            goods_item['sku_id'] = sku.xpath(r'./@goods-code').extract_first()
            goods_item['title'] = sku.xpath(r'.//div[@class="goods_txt"]//a[@target="_blank"]/text()').extract_first()
            goods_item['url'] = sku.xpath(r'.//div[@class="goods_txt"]//a[@target="_blank"]/@href').extract_first()
            goods_item['img_url'] = 'https:' + sku.xpath(r'.//a[@class="s_goods_img"]/img/@data-wpl').extract_first()

            sold = sku.xpath(r'.//div[@class="goods_sale"]/em/text()').extract_first() or ''
            goods_item['sold'] = sold.encode('utf-8').replace('销量', '')
            goods_item['price'] = sku.xpath(r'.//span[@class="s_price"]/em/text()').extract_first()
            yield goods_item

        # pagination
        url = response.url
        if '-p' not in url:
            next_page = 'https://www.wbiao.cn/shoubiao-p2.html'
        else:
            page_no = int(re.match(r'.*-p(\d+).html', url).group(1))
            next_page = 'https://www.wbiao.cn/shoubiao-p{}.html'.format(page_no+1)

        yield scrapy.Request(url=next_page, callback=self.parse, dont_filter=True)
