import time

from public.base import driver
from public.opertion_element import Element

username_password = 'el-input__inner'
click_logon = 'el-button,login-btn,el-button--primary'
class login_action(Element):

    def log_on(self,*args):

        user_mess = self.find_elements_class(username_password)
        i = 0


        user_mess[i].send_keys(args[0])

        user_mess[i+1].send_keys(args[1])


        self.find_element_class(click_logon).click()

        self.get_alter_text()


ll = login_action(driver(),'http://39.101.216.196/sdr/#/login')
ll.log_on('lijie7','12345678')