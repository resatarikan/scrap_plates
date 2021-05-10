# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 20:07:25 2021

@author: Administrator
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


def start(country, search = True, keyp ="", tip = 0, big = True, original = True):
    if big:
        prefix = "v_"
        if original:
            prefix = "vo_"
    else:
        prefix = "pm_"
    
    #default_path = "C:\\Users\\Administrator\\gd2\\shared\\"+prefix+country+"\\"
    default_path = "C:\\temp_images\\"+prefix+country+"\\"
    switcher = {
        1: "&nomer="+keyp+"*",
        2: "&ctype=" + keyp,
        3: "&dop=" + keyp,
    }
    # Get the function from switcher dictionary
    nomer = switcher.get(tip,"&nomer="+keyp+"*")

    
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
            
            pictures = driver.find_elements_by_css_selector(".col-sm-6.col-xs-12")
            
            #pictures = driver.find_elements_by_css_selector(".col-sm-6.col-xs-12 .col-xs-offset-3.col-xs-6.text-center img")
            if (len(pictures) < 2):
                print("ikinden küçük, ", len(pictures))
                break
            
            for picture in pictures:
                
                alt = picture.find_element_by_css_selector(".col-xs-offset-3.col-xs-6.text-center img").get_attribute("alt")
                if big:
                    src = picture.find_element_by_css_selector("div.row:nth-child(1) a img").get_attribute("src")
                    if original:
                        src = src.replace("/m/", "/o/")
                else:
                    src = picture.find_element_by_css_selector(".col-xs-offset-3.col-xs-6.text-center img").get_attribute("src").replace
                
                
                
                
                
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
                    if (not os.path.isfile(default_path + alt + '.png')):
                        open(default_path + alt + '.png', 'wb').write(r.content)
                        print("dosya kaydedildi >>>>>>>>>>>>", alt)
                    else:
                        print("<<<<<<<<<<<<dosya varmış", alt)
                except:
                    pass
        except:
            print("GET hatası oluştu")


for zz in range(69,91):
    for yy in range(65,91):
        print (chr(zz))
        start("de", True, chr(zz) + chr(yy), 1)
        #    start("9")



for ii in range(10):
    start("nl", True, str(ii), 1)
    #    start("9")
    
start("nl", False)
