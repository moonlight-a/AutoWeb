import os

import pytest
import yaml
from selenium import webdriver

PATH = os.path.dirname(os.path.dirname(__file__))
url_path = PATH + '//page_elements//URL.yaml'
file_open = open(url_path,'r',encoding='utf-8')
url_data = yaml.load(file_open)

def driver():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=option)
    # driver.implicitly_wait(3)
    driver.get(url_data.get('url'))
    driver.maximize_window()
    return driver




