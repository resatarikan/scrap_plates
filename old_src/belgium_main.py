# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:51:20 2021

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

options = webdriver.ChromeOptions()
#options.add_argument("--headless")

driver = webdriver.Chrome('c:\\dev\ChromeDriver\chromedriver.exe',  options=options)

default_path = "C:\\Users\\Administrator\Google Drive\\shared_files\\belgium\\"


def give_char():
    # Generate a random Uppercase letter (based on ASCII code)
    return chr(randint(65, 90))


for i in range(5000):
    try:
        plate = str(randint(1, 9)) + "-"+give_char() + give_char()+give_char() + \
            "-"+str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9))

        driver.get("https://licenceplate.be/gen/"+plate.lower()+"/long/")

        WebDriverWait(driver, 100).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".image.image-full.image-loading-bar.shadowed")))

        picture_url = driver.find_element_by_css_selector(
            ".image.image-full.image-loading-bar.shadowed").get_attribute("src")

        print(picture_url)

        # try:
        #     urllib.request.urlretrieve(picture_url, default_path+ plate.lower() + ".png")
        # except:
        #     print("indirme hatası")

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

            r = s.get(picture_url, allow_redirects=True)
            open(default_path + plate.lower() + '.png', 'wb').write(r.content)
        except:
            pass
    except:
        print('hata oluştu≠================')
