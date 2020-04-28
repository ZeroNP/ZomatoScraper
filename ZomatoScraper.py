#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:32:55 2020

@author: zeronp
"""


import urllib
from urllib import parse
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urlparse
import urllib.request
from selenium import webdriver
from bs4 import NavigableString
import sys

browser = None

try:
    browser = webdriver.Firefox()
except Exception as error:
    print(error)

out_file = open("pune_restaurant_list.txt", "ab")


class ZomatoRestaurantLinkGen:
    def __init__(self, url):
        self.url = url
        self.html_text = None
        try:
            browser.get(self.url)
            self.html_text = browser.page_source
            # self.html_text = urllib.request.urlopen(url).read().decode('utf-8')
            # self.html_text = requests.get(url).text
        except Exception as err:
            print(str(err))
            return
        else:
            print('Access successful.')

        self.soup = None
        if self.html_text is not None:
            self.soup = BeautifulSoup(self.html_text, 'lxml')

    def scrap(self):
        soup = self.soup
        for tag in soup.find_all("a", attrs={'data-result-type': 'ResCard_Name'}):
            out_file.write(tag['href'].encode('utf-8').strip() + b'\n')


if __name__ == '__main__':
    if browser is None:
        print("Selenium not opened")
        sys.exit()

    for x in range(1, 844):
        print(str(x) + '\n')
        zr = ZomatoRestaurantLinkGen('https://www.zomato.com/pune/restaurants?page={}'.format(x))
        zr.scrap()
    browser.close()
    out_file.close()