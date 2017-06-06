import re
import json
from urlparse import urlparse
import urllib
import pdb




from scrapy.selector import Selector

# from pandatv.pandatv.items import pandatvItem

try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle


from pandatv.items import *
from misc.log import *
from misc.spider import CommonSpider


# cookie = {'Cookie': 'qm_username=137958873x0; qm_sid=8a4cce2f4413b4a5c9981093942b3f6f,qMUZrWmt0Z0XQbVZWKlNBZXUzT0xCSXJNRHNXU1NDVzd6MXZFQjJSbGZxMF8.; RK=/jt+Uh72a5; pgv_pvid=2786550760; pgv_info=ssid=s5861035317; ptui_loginuin=1379588730; ptisp=ctc; ptcz=e3d339f47c356076793ff4c270b572e35ed69746057039ee2e78677e391793b9; pt2gguin=o1379588730; uin=o1379588730; skey=@ssNmMQP3p; p_uin=o1379588730; p_skey=2w78648Kd9wuwxK9lsiDM02MQFJfSIhEuxhhE*aH-SU_; pt4_token=aGGiHcty94vO0iC8mxQ*OgkHOI6fZmdzQCxsb-baX1U_'}

class pandatvSpider(CommonSpider):
    name = "pandatv"
    allowed_domains = ["panda.tv"]
    start_urls = [
        "http://www.panda.tv/all",
    ]
    rules = [
        Rule(sle(allow=("http://www.panda.tv/all")), callback='parse_1', follow=True),
    ]

    list_css_rules = { 
        '.video-list-item.video-no-tag': {
            'room_name': '.video-title::text',
            'author': '.video-nickname::text',
            'people_count': '.video-number::text',
            'tag': '.video-cate::text',
        }   
    }   

    content_css_rules = { 
        'text': '#Cnt-Main-Article-QQ p *::text',
        'images': '#Cnt-Main-Article-QQ img::attr(src)',
        'images-desc': '#Cnt-Main-Article-QQ div p+ p::text',
    }

    def parse_1(self, response):
        info('Parse '+response.url)
        x = self.parse_with_rules(response, self.list_css_rules, pandatvItem)
        # x = self.parse_with_rules(response, self.content_css_rules, pandatvItem)
        print(json.dumps(x, ensure_ascii=False, indent=2))
        # pp.pprint(x)
        # return self.parse_with_rules(response, self.css_rules, pandatvItem)

        return x
