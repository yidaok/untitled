import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://acgmoon.org/99748.html',
    ]

    def parse(self, response):
        for i  in response.xpath('/html/body/div[3]/div[1]/div[1]/div/div[2]/p[5]/img[1]'):
            yield {
                'text': str(i)}

        next_page = response.xpath('//*[@id="comments"]/div[1]/li[6]/a').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
