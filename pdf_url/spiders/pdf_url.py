import scrapy

from pdf_url.items import PdfUrlItem    # importing the data type we defined in the items.py file
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PdfUrlSpider(CrawlSpider):
    name = 'pdf_spider'

    allowed_domains = ['adobe.com']

    start_urls = ['https://www.adobe.com']

    rules = [Rule(LinkExtractor(allow=''), callback='parse_httpresponse', follow=True)]

    

    def parse_httpresponse(self, response):

        item = PdfUrlItem()
        
        # checking if url goes to pdf
        if b'Content-Type' in response.headers.keys():
            links_to_pdf = 'application/pdf' in str(response.headers['Content-Type'])

        else:
            return None

        # If it does Scrape data
        if links_to_pdf:
            print('PDF Link Found')
            print(response.url)
            print(str(response.url).split('/')[-1])
            print(links_to_pdf)
            print()
            item['filename'] = response.url.split('/')[-1]
            item['url'] = response.url

        # if not, ignore it and move on to the next link
        else:
            return None

        # write that data to the csv
        return item
