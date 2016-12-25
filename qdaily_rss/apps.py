from django.apps import AppConfig
from django.contrib.syndication.views import Feed
from .models import Article

class QdailyRssConfig(AppConfig):
    name = 'qdaily_rss'

class LatestEntriesFeed(Feed):
    title = '好奇心日报'
    link = ''
    description = '自制全文 RSS'

    def items(self):
        return Article.objects.order_by('crawled')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return item.url
