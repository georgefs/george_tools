__all__ = ['Link', 'SimpleLinkExtractor']
from bs4 import BeautifulSoup
import re
import urlparse

class Link:
    def __init__(self, url):
        self.url = url
        self.text = ""



class SimpleLinkExtractor:
    def __init__(self, allow=(), encoding="utf-8"):
        self.allow_patterns = allow
        pass

    def extract_links(self, response):
        base_url = response.url
        body = BeautifulSoup(response.body)
        link_tags = body.select('a[href]')
        return self.process_links(link_tags, base_url)

    def process_links(self, link_tags, base_url):
        for link_tag in link_tags:
            url = urlparse.urljoin(base_url, link_tag.attrs.get('href'))

            for allow_pattern in self.allow_patterns:
                if re.search(allow_pattern, url):
                    yield Link(url)

