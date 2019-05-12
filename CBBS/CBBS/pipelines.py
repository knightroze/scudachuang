# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json


def write_data_json(item, path):
    with open(path + '/' + item['title'] + '.json', 'w') as fjson:
        json.dump(dict(item), fjson)


class CbbsPipeline(object):
    def process_item(self, item, spider):
        data_path = "output/"
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        write_data_json(item, data_path)
        return item
