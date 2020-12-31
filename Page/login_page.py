import time
from public.base import driver
from public.opertion_element import Element

username_password = 'el-input__inner'
click_logon = 'el-button,login-btn,el-button--primary'
class login_action(Element):

    def log_on(self):

        user_mess = self.find_elements_class(username_password)
        for i in range(len(user_mess)):
            user_mess[i].send_keys('234')
            user_mess[i].send_keys('456')
        time.sleep(6)
        self.find_element_class(click_logon).click()

        print(self.get_alter_text())


# ll = login_action(driver(),'http://39.101.216.196/sdr/#/login')
# ll.log_on()