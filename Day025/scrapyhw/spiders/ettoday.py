import scrapy

class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net']
    start_urls = ['https://www.ettoday.net/news/20201004/1824032.htm']

    def parse(self, response):
        title = response.xpath('/xpath/of/title/').get()
        content = response.xpath('/xpath/of/content').getall()
        print(title)
        print(content)

