import os,random,time,yaml

import allure

from Page.login_page import login_action
from public.base import driver
from Tools.sql_tools import connect_sql
from selenium.webdriver.common.by import By

from public.operation_public_page import operation_page_function

PATH = os.path.dirname(os.path.dirname(__file__))


page_public_element = yaml.load(open(PATH + '//page_elements//page_public_element.yaml','r',encoding='utf-8'))
connect_sql = connect_sql()
'''查询条件元素信息'''


Select_add_organization_element = (By.XPATH,page_public_element.get('Select_add_organization_element'))
Select_add_value_elenment = (By.XPATH,page_public_element.get('Select_add_value_elenment'))
Select_add_role_element = (By.XPATH,page_public_element.get('Select_add_role_element'))
Add_Login_id_element = (By.XPATH,page_public_element.get('Add_Login_id_element'))
Add_name_element = (By.XPATH,page_public_element.get('Add_name_element'))
Add_Job_number_element = (By.XPATH,page_public_element.get('Add_Job_number_element'))
Add_Phone_element = (By.XPATH,page_public_element.get('Add_Phone_element'))
Add_Position_element = (By.XPATH,page_public_element.get('Add_Position_element'))
Add_Email_element = (By.XPATH,page_public_element.get('Add_Email_element'))

wwwwwwww = (By.XPATH,page_public_element.get('organization_test_element'))


class page_one(login_action):




    @allure.step('进入系统首页')
    @allure.description("点击页面系统管理模块，进入组织架构")
    def enter_organization(self):
        self.login_on(username='monica', password='123456')
        self.enter_moudle_name(0)
        self.operation_child_element()









if __name__ == '__main__':


    ll = page_one(driver())
    # 'username'='lijie7','password'='123456789'


    ll.enter_organization()



    # time.sleep(3)
    # ll.delete_page_screen()
    # aaa = ll.operation_delete()
    # print(aaa)
    # connect_sql.close()
