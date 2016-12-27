from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import urllib
import requests
from django.utils.timezone import now
import re

from qdaily_rss.models import Article

class Command(BaseCommand):
    help = 'do the crawling'

    def handle(self, *args, **options):
        items = []
        with urllib.request.urlopen('https://www.qdaily.com/') as url:
            soup = BeautifulSoup(url.read())
            for item in soup.find_all('a', class_='com-grid-article'):
                pattern = re.compile('/articles/(.*).html')
                id = pattern.search(item['href']).group(1)
                items.append({'url': 'https://www.qdaily.com' + item['href'],
                              'id': int(id), })
        self.process_with_raw(items)

    def process_with_raw(self, items):
        for item in items:
            with urllib.request.urlopen(item['url']) as page:
                soup = BeautifulSoup(page.read())
                content = str(soup.findAll('div', {'class': 'detail'})[0])
                title = soup.title.string
                Article.objects.get_or_create(id=item['id'],
                                                 defaults={'title': title, 'url': item['url'], 'description': content, 'crawled': now()}
                                                 )
