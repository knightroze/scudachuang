#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from CBBS.items import CbbsItem
from scrapy import FormRequest, Request
from scrapy.utils.response import open_in_browser
import re
import time


class Cbbs(CrawlSpider):
    name = "CBBS"
    # allowed_domains = ['deepcnxpfgmausrq.onion']
    # 爬虫开始进行的起始网页
    start_urls = ['http://deepmix2z2ayzi46.onion']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

    # rules = [Rule(LinkExtractor(allow=('http://deepmix2z2ayzi46.onion')),callback='login', follow=True)]

    # login
    def parse(self, response):
        return FormRequest.from_response(response, formdata={'username': 'H122333', 'password': 'Hiddenwiki122333'},
                                         callback=self.Enter_DataPage)

    # 进入“数据”栏
    def Enter_DataPage(self, response):
        page = scrapy.Selector(response)
        mainUrl = response.url
        DataPage = page.xpath('//table[@class="t_m_5"]/tr[4]/td[2]/a/@href').extract_first()
        DataPage = re.search('(http://).+(.onion)', mainUrl).group(0) + DataPage
        # print '################################'
        # print 'Enter the aim Page : '+DataPage
        # print '################################'
        return scrapy.Request(url=DataPage, headers=response.headers, dont_filter=True, callback=self.parse_pageUrls)

    # 遍历各页url（第一页、第二页...）
    def parse_pageUrls(self, response):
        for i in range(1, 26):
            pageUrl = response.url + '&pagey=' + '%d' % i + "#pagey"
            # print(pageUrl)
            yield scrapy.Request(url=pageUrl, headers=response.headers, dont_filter=True, callback=self.parse_items)

    # 遍历每页中详细条目的url
    def parse_items(self, response):
        time.sleep(5)
        item = scrapy.Selector(response)

        for each in item.xpath('/html/body/div/div[2]/div/table[2]/*//div[@class="length_400"]/a/@href').extract():
            itemUrl = re.search('(http://).+(.onion)', response.url).group(0) + each
            # print 'Enter the aim Page : ' + itemUrl
            yield scrapy.Request(url=itemUrl, headers=response.headers, dont_filter=True, callback=self.parse_content)

    # 保存评论并判断是否要翻页

    ###有个问题：爬取太频繁会重定向，如何解决？
    def parse_content(self, response):
        time.sleep(5)
        content = scrapy.Selector(response)
        item = CbbsItem()
        item['title'] = None
        item['comment'] = None
        item['value'] = None
        item['deal'] = None
        item['publictime'] = None

        title = content.xpath('/html/body/div/div[2]/div[2]/div/div/div/h3/a/text()').extract_first()
        # print title.encode('gb18030')
        if title:
            item['title'] = title

        comment = content.xpath('/html/body/div/div[2]/div[2]/div/div/div/div').extract_first()  # 一楼一定要保存，其他的怎么处理？
        # print comment.encode('gb18030')
        if comment:
            item['comment'] = comment

        value = content.xpath('/html/body/div/div[2]/form[1]/table/tr[5]/td[4]/text()').extract_first()
        if value:
            item['value'] = value

        deal = content.xpath('/html/body/div/div[2]/form[1]/table/tr[7]/td[4]/text()').extract_first()
        if deal:
            item['deal'] = deal

        publictime = content.xpath('/html/body/div/div[2]/form[1]/table/tr[3]/td[6]/text()').extract_first()
        if publictime:
            item['publictime'] = publictime

        return item
