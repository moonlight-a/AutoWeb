import os
import time

import yaml

from public.base import driver
from public.opertion_element import Element
PATH = os.path.dirname(os.path.dirname(__file__))
data_load = yaml.load(open(PATH + '//Yaml//page_element.yaml','r',encoding='utf-8'))
login_data = data_load.get('login')



class login_action(Element):

    def log_on(self,**kwargs):
        #进入页面后先截屏
        self.get_image('登录页')

        user_mess = self.find_elements_class(login_data.get('username_password'))
        i = 0

        user_mess[i].send_keys(kwargs.get('username'))
        user_mess[i+1].send_keys(kwargs.get('password'))

        self.find_element_class(login_data.get('click_logon')).click()
        time.sleep(2)

        #判断usernme或者password是否有值，决定调用alert还是tips_error

        if kwargs.get('username') ==' '  or  kwargs.get('password') == ' ':
            print(self.get_tips_error())

        elif  kwargs.get('username') !=''  and kwargs.get('password') != '':
            print(self.get_alter_text())
        else:
            print(self.get_tips_error())



if __name__ == '__main__':


    ll = login_action(driver())
    # 'username'='lijie7','password'='123456789'
    ll.log_on(username= 'lijie7',password = '12345678')