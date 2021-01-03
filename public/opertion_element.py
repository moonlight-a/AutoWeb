
#封装浏览器操作方法
import os
import datetime
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Element():

    def __init__(self,driver,url):
        self.driver = driver
        self.url = url
        self.open()

    def open(self):
        url = self.url
        self.driver.get(url)

    def find_element_class(self,loc):

        return self.driver.find_element_by_class_name(loc)

    def find_elements_class(self,loc):
        return self.driver.find_elements_by_class_name(loc)

    def find_element_by_id(self,loc):

        return self.driver.find_element_by_id(loc)

    def find_element_by_xpath(self,loc):
        return self.driver.find_element_by_xpath(loc)

    def send_keys(self,value):
        return  self.driver.send_keys(value)


    def get_alter_text(self):
            #self.driver.find_element_by_id('id').click()
            alt = Alert(self.driver)
            time.sleep(1)
            print(alt.text)
            #alter_text = self.driver.switch_to.alert




    def get_image(self):
        path = os.path.dirname(os.path.dirname(__file__))
        current_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(current_time, '%Y-%m-%d_%H-%M-%S')
        image_file = path + '//Picture//' + time_str + '.png'

        try:

            self.driver.get_screenshot_as_file(image_file)

        except BaseException as e:
            print(e)



# if __name__ == '__main__':

    # e = Element
    # w = e.find_element_class('el-input__inner')
    # print(w)