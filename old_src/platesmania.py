

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:09:58 2021

@author: Richard Gold
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import requests

import urllib.request
import json
import os
from random import randint

driver = webdriver.Chrome('c:\\dev\ChromeDriver\chromedriver.exe')

country = "iy"



default_path = "C:\\Users\\Administrator\\Google Drive\\shared_files\\pm_last\\pm_"+country+"\\"


search = True



def start(keyp):
    nomer = "&nomer="+keyp+"*"
    # nomer = "&ctype=" + keyp
    
    # nomer = "&dop=" + keyp
    
    base_url="http://platesmania.com/"+country+"/gallery"
    #http://platesmania.com/nl/gallery.php?&nomer=a*&start=1
    #http://platesmania.com/it/gallery.php?gal=it&ctype=1
    search_url = "http://platesmania.com/"+country+"/gallery.php?"+nomer
    if search:
        aralik = "&start="
        ll_url = search_url
    else:
        aralik = "-"
        ll_url = base_url
    
    
    for i in range(101):
        if i == 0:
            l_url = ll_url
        else: l_url = ll_url + aralik + str(i)
         
        print (l_url)
        try:
            
            driver.get(l_url)
            pictures = driver.find_elements_by_css_selector(".col-sm-6.col-xs-12 .col-xs-offset-3.col-xs-6.text-center img")
            if (len(pictures) < 2):
                print("ikinden küçük, ", len(pictures))
                break
            
            for picture in pictures:
                
                src = picture.get_attribute("src")
                
                
                print(src)
                try:
                
                    headers = {
                        "User-Agent":
                        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
                    }
                    s = requests.session()
                    s.headers.update(headers)
                
                    for cookie in driver.get_cookies():
                        c = {cookie['name']: cookie['value']}
                        s.cookies.update(c)
                
                    r = s.get(src, allow_redirects=True)
                    open(default_path + picture.get_attribute("alt") + '.png', 'wb').write(r.content)
                except:
                    pass
        except:
            print("GET hatası oluştu")


for zz in range(65,91):
    print (chr(zz))
    start(chr(zz))
    
#    start("0")


for ii in range(8,11):
    start(str(ii))