import scrapy

from pdf_url.items import PdfUrlItem    # importing the data type we defined in the items.py file
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PdfUrlSpider(CrawlSpider):
    # This is required and this is how we refer to the spider form commandline
    name = 'pdf_spider'

    # List of domains that spider is allowed to scrape
    allowed_domains = ['adobe.com']

    # Spider statrts to crawl from this url
    start_urls = ['https://www.adobe.com']

    #   This RULE says:
    #   Allows all the links that cam be scraped.
    #   Call parse_httpresponse on every extracted link.
    #   Follow all links (click on them)to find more links.
    rules = [Rule(LinkExtractor(allow=''), callback='parse_httpresponse', follow=True)]

    
    def parse_httpresponse(self, response):
        # Checking server response
        if response.status != 200:
            return None


        item = PdfUrlItem()

        # checking if url goes to pdf
        if b'Content-Type' in response.headers.keys():
            # Boolian
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
