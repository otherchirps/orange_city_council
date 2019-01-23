#!/usr/bin/env python

import os
# morph.io requires this db filename, but scraperwiki doesn't nicely
# expose a way to alter this. So we'll fiddle our environment ourselves
# before our pipeline modules load.
os.environ['SCRAPERWIKI_DATABASE_NAME'] = 'sqlite:///data.sqlite'

from scrapy import log
#from orange_city_council.spiders.planningalerts import PlanningalertsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
#log.start(loglevel=log.INFO)

process.crawl('planningalerts', domain='ecouncil.orange.nsw.gov.au')
process.start() # the script will block here until the crawling is finished

