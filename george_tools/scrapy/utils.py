__all__ = ['set_job_info',]

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
