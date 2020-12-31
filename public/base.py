
from selenium import webdriver


def driver():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=option)

    return driver



