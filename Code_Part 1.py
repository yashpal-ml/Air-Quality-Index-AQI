# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 10:08:45 2019

@author: YSHARMA
"""

import os
import time
import requests #helps to download page in HTML format
import sys

#function to retrieve html data from en.tutiempo.net
def retrieve_html():
    for year in range(2013, 2019):
        for month in range(1,13):
            if(month<10):
                url = 'http://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month, year)
            else:
                url = 'http://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month, year)
    
            texts = requests.get(url) #download data in HTML
            
            #utf encoding - to fix the characters in the html tags
            text_utf = texts.text.encode('utf=8')
            
            if not os.path.exists("Data/Html_Data/{}" .format(year)): #folder creation for every year
                os.makedirs("Data/Html_Data/{}".format(year))
            
            with open("Data/Html_Data/{}/{}.html".format(year,month), "wb") as output: #insert data to files
                output.write(text_utf)
        
        sys.stdout.flush()
        
if __name__ =="__main__":
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    
    time_taken = stop_time - start_time
    print("Time taken {}".format(time_taken))