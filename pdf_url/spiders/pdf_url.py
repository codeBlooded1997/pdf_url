import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


# scrapy.Spider (basic spider | Doesn't require rules method to define)
class PdfUrlSpider(CrawlSpider):

    # This is required. It how I refer to this PdfUrlSpider class on the command line.
    name = 'pdf_url'

    # Optional (just doamin name no https:// required)
    # Every link we look at MUST be a part of the adobe.com domain (i.e contain "adobe.com" in it's url)
    allowed_domains = ['adobe.com']

    # Url we want to start scraping from
    start_urls = ['https://www.adobe.com']

    # Required for CrawlSpider
    # allow all links to be extracted
    # call parse_httpresponse on each extracted link
    # follow all links ("click on them") so we can check all the links on THAT webpage too
    rules = [Rule(LinkExtractor(allow=''), callback='parse_httpresponse', follow=True)]

    # When ever we extarct the allowed links we gonn asend it to this funcion to proccess
    def parse_httpresponse(self, response):
        # response holds all the data we got back from spider
        print(response)
        


        # check if the link goes to a pdf

        # if it does, scrape it

        # if not, ignore it and move on to the next link

        # write that data to the csv

        return
