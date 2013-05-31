__all__ = ['set_jobid',]

import os
def set_jobid(spider_class):
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
        self.jobid = os.environ.get('SCRAPY_JOB', "")
        super(spider_class, self).__init__(*args, **kwargs)

    spider_class.__init__ = __init__
    return spider_class
