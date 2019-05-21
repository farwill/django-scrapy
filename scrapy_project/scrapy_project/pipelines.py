# -*- coding: utf-8 -*-
from quote_app.models import Tag, Quote
from scrapy_project.items import QuoteItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyProjectPipeline(object):
    def process_item(self, item, spider):
        return item

class QuotePipeline(object):
    def process_item(self, item, spider):
        if not isinstance(item, QuoteItem):
            return item
        else:
            item.save()
            for tag_name in item['tag_list']:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                quote = Quote.objects.get(title=item['title'], author=item['author'])
                quote.tags.add(tag)
        return item
