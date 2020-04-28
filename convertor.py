#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:21:05 2020

@author: zeronp
"""

import json 
import csv 
  
  
# Opening JSON file and loading the data 
# into the variable data 
with open('zomato_pune.json') as json_file: 
    data = json.load(json_file) 
  
restaurants_data = data['restaurants'] 
  
# now we will open a file for writing 
data_file = open('zomato_pune.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 

  
header = ['name','reviews_count','contact','facilities','timing','address','known_for','restaurant_facilities','costing','top_dishes','other'] 
csv_writer.writerow(header) 
for r in restaurants_data: 
      # Writing data of CSV file 
    csv_writer.writerow(r.values()) 
  
data_file.close() 