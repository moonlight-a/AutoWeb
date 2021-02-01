import os
import re
import time

import yaml

from public.base import driver
from public.opertion_element import Element
from selenium.webdriver.common.by import By
PATH = os.path.dirname(os.path.dirname(__file__))
login_page_element = yaml.load(open(PATH + '//page_elements//page_login_element.yaml','r',encoding='utf-8'))
username_element = (By.XPATH,login_page_element.get('username_element'))
password_element = (By.XPATH,login_page_element.get('password_element'))
logon_button_element = (By.CLASS_NAME,login_page_element.get('logon_button_element'))

class login_action(Element):

    def log_on(self,**kwargs):
        curr_url = self.get_currernt_url()
        user_mess = self.find_element_by_xpath(username_element)
        pass_mess = self.find_element_by_xpath(password_element)
        user_mess.send_keys(kwargs.get('username'))
        pass_mess.send_keys(kwargs.get('password'))
        self.find_element_class(logon_button_element).click()
        operation_url = self.get_currernt_url()

        #判断usernme或者password是否有值，决定调用alert还是tips_error

        if kwargs.get('username') =='' or kwargs.get('password')=='':
             print(self.get_tips_error())
             return self.get_tips_error()

        elif   (kwargs.get('username') =='') and (kwargs.get('password')==''):
            print(self.get_tips_error())
            return self.get_tips_error()

        elif curr_url != operation_url:
            print('登录成功')
            return True

        else:
            print(self.get_alter_text())
            return self.get_alter_text()



if __name__ == '__main__':


    ll = login_action(driver())
    # 'username'='lijie7','password'='123456789'
    www =ll.log_on(username= '',password = '')
    print(www)