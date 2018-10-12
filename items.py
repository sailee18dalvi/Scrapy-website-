# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

###########################################################

class NewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    #Main Fields
    main_headline = Field()
    headline = Field()


    #Separate Fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()

    #Location Fields
    #location = Field()

#######################################################

class TestItem(scrapy.Item):

    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()

#######################################################

class MovieItem(scrapy.Item):

	#defining item fields
    title = scrapy.Field()
    directors = scrapy.Field()
    writers = scrapy.Field() 
    stars = scrapy.Field()
    popularity = scrapy.Field()
##############################################################


class RealNewsItem(scrapy.Item):

	#defining item fields
    title = scrapy.Field()
    description = scrapy.Field()
    image = scrapy.Field() 
    author = scrapy.Field()
    date = scrapy.Field()
    channel = scrapy.Field()

