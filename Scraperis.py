import json

import jsonlines
import scrapy
from scrapy.crawler import CrawlerProcess
import os

if os.path.exists('scrapedCars.json'):
    os.remove('scrapedCars.json')

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'scrapedCars.json',
    'FEED_EXPORT_ENCODING': 'utf-8'
})


class CarsSpider(scrapy.Spider):
    name = 'cars'
    start_urls = [
        'https://autogidas.lt/skelbimai/automobiliai/?f_1%5B0%5D=&f_model_14%5B0%5D=&f_215=&f_216=&f_41=&f_42=&f_376='
    ]
    base_url = 'https://autogidas.lt'

    count = 0
    countMax = 35

    def parse(self, response):
        carListItems = response.xpath("//div[@class='list-item']")

        for car in carListItems:
            carFromListUrl = self.base_url + car.xpath(".//a/@href").extract_first()

            req = scrapy.Request(carFromListUrl, callback=self.parse_subcategory)

            if self.count < self.countMax:
                self.count += 1
                yield req

        if self.count < self.countMax:
            nextPageUrl = self.base_url + response.xpath(
                "//div[@class='next-page-block no-print']/a/@href").extract_first()
            yield scrapy.Request(nextPageUrl, callback=self.parse)

    def parse_subcategory(self, response):

        yield {
            "Brand": response.xpath(
                "normalize-space(.//div[@class='params-block']/div[@class='param']/*[contains(text(),'Markė')]/../div[@class='right']/text()[1])").extract_first(),
            "Model": response.xpath(
                "normalize-space(.//div[@class='params-block']/div[@class='param']/*[contains(text(),'Modelis')]/../div[@class='right']/text()[1])").extract_first(),
            "Year": response.xpath(
                "normalize-space(.//div[@class='params-block']/div[@class='param']/*[contains(text(),'Metai')]/../div[@class='right']/text()[1])").extract_first(),
            "Price": response.xpath(".//div[@class='price']/text()[1]").extract_first().strip(),
            "Engine": response.xpath(
                "normalize-space(.//div[@class='params-block']/div[@class='param']/*[contains(text(),'Variklis')]/../div[@class='right']/text()[1])").extract_first(),
            "Fuel Type": response.xpath(
                "normalize-space(.//div[@class='params-block']/div[@class='param']/*[contains(text(),'Kuro tipas')]/../div[@class='right']/text()[1])").extract_first(),
            "Body Type": response.xpath(
                "normalize-space(.//div[@class='params-block']/div[@class='param']/*[contains(text(),'Kėbulo tipas')]/../div[@class='right']/text()[1])").extract_first(),
            "Gearbox": response.xpath(
                "normalize-space(.//div[@class='params-block']/div[@class='param']/*[contains(text(),'Pavarų dėžė')]/../div[@class='right']/text()[1])").extract_first(),
            "Damage": response.xpath(
                "normalize-space(.//div[@class='params-block']/div[@class='param']/*[contains(text(),'Defektai')]/../div[@class='right']/text()[1])").extract_first(),
            "Steering column": response.xpath(
                "normalize-space(.//div[@class='params-block']/div[@class='param']/*[contains(text(),'Vairo padėtis')]/../div[@class='right']/text()[1])").extract_first(),
            "Doors": response.xpath(
                "normalize-space(.//div[@class='params-block']/div[@class='param']/*[contains(text(),'Durų skaičius')]/../div[@class='right']/text()[1])").extract_first(),
            "TS to": response.xpath(
                "normalize-space(.//div[@class='params-block']/div[@class='param']/*[contains(text(),'TA iki')]/../div[@class='right']/text()[1])").extract_first(),
            "Main Photo": response.xpath(
                "//div[@class='right-media']/div[@class='big-photo']/img/@src").extract_first(),
            "Photos": response.xpath(
                "//div[@class='mini-container']/div[@class='photo photo-type-image ']/@data-src").extract()
        }


process.crawl(CarsSpider)

process.start()

import json

# with open("scrapedCars.json","r") as f:
#     data = f.read()
#
# datas = data.items()
#
#     newlist = sorted(data, key=lambda x: x.count,
#
# print(data)
import json

with open("scrapedCars.json") as file:
  data = json.load(file)

  # print(data)

  sorted_list = sorted(data, key=lambda k: k['Brand'])

print(sorted_list)



with open("4forces.json", 'w') as file:
  json.dump(data, file)

print(data)


data.sort(key=lambda itms: (itms['Brand'], itms['Model'], itms['Year']))

sorted_list = sorted(data, key=lambda k: (str(k['Brand']), str(k["Model"])))




sortedq_obj = sorted(data, key=lambda i: (i['Brand'], i['Model'], i['Year'], i['Price']))



with open("4forces.json", "w") as f:
    f.write(sortedq_obj)
    sorted_obj = dict(data)
    # sorting = sorted(data, key=lambda i: (i['Brand'], i['Model'], i['Year'], i['Price']))
print(data)

    with open("4forces.json", "w") as f:
        f.write(data)

    # print(sorting)



# with open('scrapedCars.json', 'w') as json_data:
#
#     scrapedCarsList = json.load(json_data)
#      sorting = sorted(scrapedCarsList, key=lambda i: (i['Brand'], i['Model'], i['Year'], i['Price']))
#     print(json.dumps(scrapedCarsList, indent=2))

# data = jsonlines.open('scrapedCars.json')
