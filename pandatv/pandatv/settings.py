# Scrapy settings for pandatv project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import sys
import os
from os.path import dirname
path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)
from misc.log import *

BOT_NAME = 'pandatv'

SPIDER_MODULES = ['pandatv.spiders']
NEWSPIDER_MODULE = 'pandatv.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pandatv (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
   # 'misc.middleware.CustomHttpProxyMiddleware': 400,
    'misc.middleware.CustomUserAgentMiddleware': 401,
}

ITEM_PIPELINES = {
    'pandatv.pipelines.JsonWithEncodingPipeline': 300,
    #'pandatv.pipelines.RedisPipeline': 301,
}

LOG_LEVEL = 'DEBUG'

DOWNLOAD_DELAY = 3

ROBOTSTXT_OBEY = False

COOKIES_ENABLED = True

COOKIES_DEBUG = True


DEFAULT_REQUEST_HEADERS = {
    'accept': 'image/webp,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.8',
    'referer': 'https://www.taobao.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
}