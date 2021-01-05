
#封装浏览器操作方法
import os
import datetime
import time

import yaml

PATH = os.path.dirname(os.path.dirname(__file__))
open_data = open(PATH + '//Yaml//page_element.yaml','r',encoding='utf-8')
read_data = yaml.load(open_data)

from public import base


class Element():

    def __init__(self,driver):
        self.driver = driver


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

        time.sleep(1)
        alert_text  = self.find_element_class(read_data.get('alert_element'))



        return alert_text.text

    def get_tips_error(self):
        #由于文本框存在多个值需将错误提示语封装到list
        list_error = []
        time.sleep(1)
        error_text = self.find_elements_class(read_data.get('tips_element'))

        print(error_text,'22222222222222222222222222')
        if len(error_text) > 1:
            for text in range(len(error_text)):
                list_error.append(error_text[text].text)
            return set(list_error)
        else:
            return error_text[0].text


    def get_image(self):
        path = os.path.dirname(os.path.dirname(__file__))
        current_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(current_time, '%Y-%m-%d_%H-%M-%S')
        image_file = path + '//Picture//' + time_str + '.png'

        try:

            self.driver.get_screenshot_as_file(image_file)

        except BaseException as e:
            print(e)



if __name__ == '__main__':

    e = Element(base.driver())
    w = e.get_alter_text()
    print(w)