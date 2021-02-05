
#封装浏览器操作方法
import os, datetime,time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public import base

class Element():

    def __init__(self,driver):
        self.driver = driver


    def find_element_class(self,*loc):
        element = WebDriverWait(self.driver,5,0.5).until(
            EC.presence_of_element_located(*loc))
        return element

    def find_elements_class(self,*loc):
        element = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_all_elements_located(*loc))
        return element

    def find_element_by_id(self,*loc):
        element = WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located(*loc))
        return element

    def find_element_by_xpath(self,*loc):
        element = WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located(*loc))
        return element

    def find_elements_by_xpath(self,*loc):
        element = WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_all_elements_located(*loc))
        return element

    def find_element_by_link_text(self,*loc):
        link_text_element = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(*loc))
        return link_text_element




# 获取页面当前url
    def get_currernt_url(self):


        return self.driver.current_url

#截图操作
    def get_image(self,pagename):
        path = os.path.dirname(os.path.dirname(__file__))
        current_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(current_time, '%Y-%m-%d_%H-%M-%S')
        image_file = path + '//Picture//'  + pagename + '_' +time_str + '.png'

        try:

            self.driver.get_screenshot_as_file(image_file)

        except BaseException as e:
            print(e)

#操作需要鼠标悬浮显示元素值
    def mouse_action(self,aa):

        ActionChains(self.driver).move_to_element(aa).click(aa).perform()
        # time.sleep(2)
        # self.find_element_by_link_text(operation_text).click()
        return None

if __name__ == '__main__':

    e = Element(base.driver())
    w = e.tree_button_element()
    print(w)