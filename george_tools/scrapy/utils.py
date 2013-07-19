__all__ = ['set_job_info', 'close_job', 'open_spider']

import urlparse
import os

from george_tools.utils import system as system_util


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


def close_job(project, jobid, host="http://localhost:6800", time='now'):
    url = urlparse.urljoin(host, 'cancel.json')

    script = '''
    curl {} -d project={} -d job={}
    '''.format(url, project, jobid)

    system_util.at(time, script)


def open_spider(project, spider, host="http://localhost:6800", time='now'):
    url = urlparse.urljoin(host, 'schedule.json')

    script = '''
    curl {} -d project={} -d spider={}
    '''.format(url, project, spider)

    system_util.at(time, script)
