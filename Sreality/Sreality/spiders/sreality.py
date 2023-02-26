import scrapy
from Sreality.items import SrealityItem

class SrealitySpider(scrapy.Spider):
    name = 'Sreality'
    allowed_domains = ['sreality.cz']
    start_urls = [f'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500&sort=0']

    def parse(self, response):
        data = response.json()
        estates = data['_embedded']['estates']
        for estate in estates:
            item = SrealityItem()
            image_url = estate['_links']['dynamicDown'][0]['href'].replace('{width}', '400').replace('{height}', '300')
            item['title'] = estate['name']
            item['img_url'] = image_url
            yield item