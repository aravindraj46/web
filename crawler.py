# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:38:41 2018

@author: aravindraj.m
"""

import pandas as pd
from selenium import webdriver as wd
import logging

df = pd.read_csv("D:/eComm_crawler_19oct.csv")
driver = wd.Chrome(executable_path="D:/chromedriver.exe")
driver.get("https://gskstaging9:Respect18@gskhealthpartner-com-preprod-cf5.gdsgsk.com/en-gb/")
driver.maximize_window()

data = []
for i in range(df.shape[0]):
    driver.implicitly_wait(4000)
    driver.get(df["URL"][i])
    driver.implicitly_wait(4000)
    print("URL is : {}", format(df["URL"][i]))
    k=driver.find_element_by_xpath(df["Title"][i]).text
    print("text is : {}", format(k))
    data.append(k)
   
        
    
logging.basicConfig(filename='./applog.log', filemode='a', 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

    