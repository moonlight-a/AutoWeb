import os
import re
import time
import allure
import yaml

from public.base import driver
from public.operation_public_page import operation_page_function

from selenium.webdriver.common.by import By
PATH = os.path.dirname(os.path.dirname(__file__))
login_page_element = yaml.load(open(PATH + '//page_elements//page_login_element.yaml','r',encoding='utf-8'))
username_element = (By.XPATH,login_page_element.get('username_element'))
password_element = (By.XPATH,login_page_element.get('password_element'))
logon_button_element = (By.CLASS_NAME,login_page_element.get('logon_button_element'))

class login_action(operation_page_function):

    def login_on(self,**kwargs):
        self.curr_url = self.get_currernt_url()
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        user_mess = self.find_element_by_xpath(username_element)
        pass_mess = self.find_element_by_xpath(password_element)
        user_mess.send_keys(self.username)
        pass_mess.send_keys(self.password)
        self.find_element_class(logon_button_element).click()
        time.sleep(1)
    #检查登录状态

    def check_login_status(self):
        operation_url = self.get_currernt_url()
        #判断usernme或者password是否有值，决定调用alert还是tips_error
        if self.curr_url != operation_url:
            return True
        elif self.username =='' and  self.password =='':
             return self.get_tips_error()
        elif  self.username =='' or  self.password =='':
            return self.get_tips_error()
        else:
            return self.get_alter_text()


if __name__ == '__main__':


    ll = login_action(driver())
    # 'username'='lijie7','password'='123456789'
    www =ll.login_on(username= 'monica',password = '123456')
    wwwwww = ll.check_login_status()
    print(wwwwww)
