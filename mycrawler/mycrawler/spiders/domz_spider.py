import scrapy

#Spiders are classes that you define and Scrapy uses to scrape information from
# a domain (or group of domains).
#They define an initial list of URLs to download, how to follow links, and how 
#to parse the contents of pages to extract items.
class DomzSpider(scrapy.Spider):
    name = "domz" 
    allowed_domains=["domz.org"]
    #Scrapy creates scrapy.Request objects for each URL in the start_urls attribute of the Spider,
    # and assigns them the parse method of the spider as their callback function.
    starts_urls= [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]
       
    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print title, link, desc
            
