import scrapy

from pdf_url.items import PdfUrlItem    # importing the data type we defined in the items.py file
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PdfUrlSpider(CrawlSpider):
    name = 'pdf_spider'

    allowed_domains = ['adobe.com']

    start_urls = ['https://www.adobe.com']

    rules = [Rule(LinkExtractor(allow=''), callback='parse_httpresponse', follow=True)]

    item = PdfUrlItem()

    

    def parse_httpresponse(self, response):
        print(response.url)
        print()

        # checking if url goes to pdf
        if b'Content-Type' in response.headers.keys():
            goes_to_pdf = 'application/pdf' in str(response.headers['Content-Type'])
        else:
            return None

        if goes_to_pdf:
            item['filename'] = response.url.split('/')[-1]
            item['url'] = response.url
            print('Link found')
            print(response.url)
            print(goes_to_pdf)
            print()
            print()
            print()
            print()
            ptint()

        else:
            return None






# scrapy.Spider (basic spider | Doesn't require rules method to define)
#class PdfUrlSpider(CrawlSpider):

    # This is required. It how I refer to this PdfUrlSpider class on the command line.
    #name = 'pdf_url'

    # Optional (just doamin name no https:// required)
    # Every link we look at MUST be a part of the adobe.com domain (i.e contain "adobe.com" in it's url)
    #allowed_domains = ['adobe.com']

    # Url we want to start scraping from
    #start_urls = ['https://www.adobe.com']

    # Required for CrawlSpider
    # allow all links to be extracted
    # call parse_httpresponse on each extracted link
    # follow all links ("click on them") so we can check all the links on THAT webpage too
    #rules = [Rule(LinkExtractor(allow=''), callback='parse_httpresponse', follow=True)]

    # When ever we extarct the allowed links we gonn asend it to this funcion to proccess
    #def parse_httpresponse(self, response):
        #print(response.url)
        #print(response.headers.split('/')[-1])
        #print()
        #item = PdfUrlItem()     # for saving scraped data

        # check if the link goes to a pdf
        #if b'Content-Type' in response.headers.keys():
        #    links_to_pdf = 'application/pdf' in str(response.headers['Content-Type'])
        #else:
        #    return None

        # if it does, scrape it
        #if links_to_pdf:
        #    item['filename'] = response.url.split('/')[-1]
        #    item['url'] = response.url
        # if not, ignore it and move on to the next link
        #else:
        #    return None


        # write that data to the csv
        #return
