import os
from selenium import webdriver
import yaml
PATH = os.path.dirname(os.path.dirname(__file__))
yaml_path = open(PATH + '//Yaml//URL.yaml','r',encoding='utf-8')
url_yaml = yaml.load(yaml_path)

def driver():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=option)
    return driver



