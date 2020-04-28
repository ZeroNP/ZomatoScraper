
import re
import urllib
from urllib import parse
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib.request
from selenium import webdriver
from bs4 import NavigableString
import sys
import json
from selenium.webdriver.firefox.options import Options
import csv


browser = None
try:
    #options = Options()
    #options.add_argument('-headless')
    browser = webdriver.Firefox()
except Exception as error:
    print(error)


class ZomatoRestaurant:
    def __init__(self, url):
        self.url = url
        # print("opening")
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
            print('Access successful to ',url)

        self.soup = None
        if self.html_text is not None:
            self.soup = BeautifulSoup(self.html_text, 'lxml')

    def scrap(self):
        if self.soup is None:
            return {}
        soup = self.soup
        rest_details = dict()
        last_slash = self.url.rfind("/") + 1
        rest_details['name'] = self.url[last_slash:-1]
                                                             
        rating_div = soup.find("p", attrs={"class": "sc-1hez2tp-0 sSutT"})
        if rating_div:
            rest_details['rating'] = rating_div.text.strip()
        else:
            rest_details['rating'] = 'N'  # default

        reviews_count = soup.find("p", attrs={"class": "sc-1hez2tp-0 fcbEvV"})
        if reviews_count:
            rest_details['reviews_count'] = reviews_count.text.strip()[:-8]
        else:
            rest_details['reviews_count'] = '0' 
            
        rest_details['contact']=[]
        for contact_span in soup.findAll("p", attrs={"class": 'sc-1hez2tp-0 kKemRh'}):
            if contact_span:
                rest_details['contact'].append(contact_span.text.strip())

                
        res_info = []
        for it in soup.findAll("p", attrs={'class': 'sc-1hez2tp-0 cunMUz'}):
            try:
                res_info.append(it.text.strip())
            except NavigableString:
                pass
        rest_details['facilities'] = res_info

        week_schedule = soup.find("span", attrs={"class": "sc-ivVeuv fDPsPR"})
        if week_schedule:
            rest_details['timing'] = week_schedule.text.strip().replace("\u2013","-")
        else:
            rest_details['timing'] = ''


        address_div = soup.find("p", attrs={"class": "sc-1hez2tp-0 clKRrC"})
        if address_div:
            rest_details['address'] = address_div.text.strip()
        else:
            rest_details['address'] = ""

        known_for_div = soup.find("a", attrs={'class': 'sc-jvEmr ieuMKS'})
        if known_for_div:
            rest_details['known_for'] = known_for_div.text.strip()
        else:
            rest_details['known_for'] = ''

        rest_details['restaurant_facilities'] = []
        for div in soup.find_all("p", attrs={'class': 'sc-1hez2tp-0 fvARMW'}):
            if div:
                rest_details['restaurant_facilities'].append(div.get_text())
                
            
        rest_details['top_dishes_and_other'] = []
        rest_details['costing'] = ''
        other_data = soup.findAll("p", attrs={"color": "#4F4F4F"})
        for it in other_data:
            text_val = it.get_text()
            if "for" in text_val and "people" in text_val:
                rest_details['costing'] = text_val.replace("\u20b9","Rs. ")
            else:
                rest_details['top_dishes_and_other'].append(text_val)
        
        return rest_details


if __name__ == '__main__':
    if browser is None:
        sys.exit()
    out_file = open("zomato_pune.json", "a")
    with open('pune_restaurant_list.txt', 'r', encoding="utf-8") as f:
        for line in f:
            zr = ZomatoRestaurant(line)
            json.dump(zr.scrap(), out_file)
            out_file.write(',\n')
    out_file.close()
    
     #values row
    browser.close()