#!/usr/bin/env python

import os, sys
import scrapy
import csv

# https://www.eventbrite.hk/d/germany--berlin/events/

# # name
# //*[@id="root"]/div/div[2]/div/div/main/section/main/div/div[1]/div/div/div[2]/div[1]/div/div/div/section/main/div[1]/div[2]/div[1]/a/h3/div/div[2]
# //*[@id="root"]/div/div[2]/div/div/main/section/main/div/div[1]/div/div/div[2]/div[2]/div/div/div/section/main/div[1]/div[2]/div[1]/a/h3/div/div[2]
# //*[@id="root"]/div/div[2]/div/div/main/section/main/div/div[4]//div/div/div[2]/div[6]/div/div/div/section/main/div[1]/div[2]/div[1]/a/h3/div/div[2]/text()

# # date
# //*[@id="root"]/div/div[2]/div/div/main/section/main/div/div[1]/div/div/div[2]/div[1]/div/div/div/section/main/div[1]/div[2]/div[2]/div[1]
#
# //*[@id="root"]/div/div[2]/div/div/main/section/main/div/div[1]/div/div/div[2]/div[2]/div/div/div/section/main/div[1]/div[2]/div[2]/div[1]

# # location
# //*[@id="root"]/div/div[2]/div/div/main/section/main/div/div[1]/div/div/div[2]/div[1]/div/div/div/section/main/div[1]/div[2]/div[2]/div[2]/div[1]/div
# //*[@id="root"]/div/div[2]/div/div/main/section/main/div/div[1]/div/div/div[2]/div[2]/div/div/div/section/main/div[1]/div[2]/div[2]/div[2]/div[1]/div

EVENT_BRITE_URL="https://www.eventbrite.hk/d/germany--berlin/events/"


XPATH_CARD_GROUP='//*[@id="root"]/div/div[2]/div/div/main/section/main/div/div[%d]'
XPATH_PER_CARD = '%s/div/div/div[2]/div[%d]/div/div/div/section/main/div[1]/div[2]'
XPATH_EVENT_NAME ='%s/div[1]/a/h3/div/div[2]/text()'
XPATH_EVENT_DATE ='%s/div[2]/div[1]/text()'
XPATH_EVENT_PLACE ='%s/div[2]/div[2]/div[1]/div/text()'

COL_NAME_EVENT_NAME='event name'
COL_NAME_EVENT_DATE='event date'
COL_NAME_EVENT_LOCATION='event location'

csv_col_names = [COL_NAME_EVENT_NAME, COL_NAME_EVENT_DATE,COL_NAME_EVENT_LOCATION]

CSV_OUTPUT_FILE='./test_event.csv'

def get_card_xpath(i,j):
    XPATH_TO_CARD = XPATH_PER_CARD % (XPATH_CARD_GROUP % i , j)
    return XPATH_TO_CARD

def create_csv(col_name, csv_filename):
    with open(csv_filename,'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=col_name)
        writer.writeheader()

def write_csv(d_event, col_name, csv_filename):
    with open(csv_filename,'a+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=col_name)
        writer.writerow(d_event)


class EventBriteSpider(scrapy.Spider):
    name = "EventBrite"
    # start_urls = [EVENT_BRITE_URL]

    def start_requests(self):
        return [scrapy.FormRequest(EVENT_BRITE_URL,callback=self.csv_parser)]

    def csv_parser(self, response):
        create_csv(csv_col_names,CSV_OUTPUT_FILE)
        for i in range(1,4+1):
            for j in range(1,6+1):
                XPATH_TO_CARD = get_card_xpath(i,j)
                d_event= {
                    COL_NAME_EVENT_NAME:response.xpath(XPATH_EVENT_NAME % XPATH_TO_CARD).extract_first(),
                    COL_NAME_EVENT_DATE:response.xpath(XPATH_EVENT_DATE % XPATH_TO_CARD).extract_first(),
                    COL_NAME_EVENT_LOCATION:response.xpath(XPATH_EVENT_PLACE % XPATH_TO_CARD).extract_first(),
                }
                write_csv( d_event,csv_col_names, CSV_OUTPUT_FILE)
