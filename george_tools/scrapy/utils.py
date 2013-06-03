__all__ = ['set_job_info', 'close_job', 'open_spider']
import urllib2, urllib
import urlparse
import os
def set_job_info(spider_class):
    '''
    simple way to add scrapyd's jobid into spider

    simple code

    >@set_jobid
    >class mySpider(BaseSpider):
    >    pass
    >
    >print mySpider().jobid

    '''
    def __init__(self, *args, **kwargs):
        job_info = dict()
        job_info['id'] = os.environ.get('SCRAPY_JOB', '')
        job_info['project'] = os.environ.get('SCRAPY_PROJECT', '')
        job_info['log'] = os.environ.get('SCRAPY_LOG_FILE', '')
        job_info['data'] = os.environ.get('SCRAPY_FEED_URI', '')

        self.job_info = job_info
        super(spider_class, self).__init__(*args, **kwargs)

    spider_class.__init__ = __init__
    return spider_class

def close_job(project, jobid, host="http://localhost:6800"):
    url = urlparse.urljoin(host, 'cancel.json')
    data = dict()
    data['project'] = project
    data['job'] = jobid

    data_str = urllib.urlencode(data)
    req = urllib2.Request(url, data_str)
    urllib2.urlopen(req)

def open_spider(project, spider, host="http://localhost:6800"):
    url = urlparse.urljoin(host, 'schedule.json')
    data = dict()
    data['project'] = project
    data['spider'] = spider

    data_str = urllib.urlencode(data)
    req = urllib2.Request(url, data_str)
    urllib2.urlopen(req)
