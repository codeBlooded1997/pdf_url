import scrapy

from scrapy.spiders import CrawlSpider


# scrapy.Spider (basic spider | Doesn't require rules method to define)
class PdfUrlSpider(CrawlSpider):

    # Neccesery
    name = 'pdf_url'

    # Optional (just doamin name no https:// required)
    allowed_domains = ['adobe.com']

    # Url we want to start scraping from
    start_urls = ['https://www.adobe.com']

    # Required for CrawlSpider
    # Rules that we have to follow for an specific link
    # Any other link other than the alowed ones in Rule are going to be ignored (blank means all links are allowded)
    # callback takes the fuction that we want to run on the extracted link
    # follow means we are going to follow(recurse) every single link that we had extracted in the defined domain
    rules = [Rule(LinkExtractor(allow=''), callback='parse_httpresponse', follow=True)]

    # When ever we extarct the aloowed links we gonn asend it to this funcion to proccess
    def parse_httpresponse():



        return
