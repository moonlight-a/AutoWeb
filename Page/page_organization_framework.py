import os,time,yaml, allure
from Page.login_page import login_action
from public.base import driver
from Tools.sql_tools import connect_sql
from selenium.webdriver.common.by import By
PATH = os.path.dirname(os.path.dirname(__file__))
organ_framework = yaml.load(open(PATH + '//page_elements//page_organization_element.yaml','r',encoding='utf-8'))

#添加组织
ADD_ORGANIATION_BUTTON = (By.XPATH,organ_framework.get('Add_organization_element'))
#组织名称
ORGANIATION_NAME = (By.XPATH,organ_framework.get('Add_organization_name_element'))
#组织编号
ORGANIATION_ID = (By.XPATH,organ_framework.get('Add_organization_id_element'))
#组织确定提交按钮
ADD_ORGANIATION_CONFIRM_BUTTON = (By.XPATH,organ_framework.get('Add_organization_confirm_element'))

class page_one(login_action):

    @allure.step('进入系统首页')
    @allure.description("点击页面系统管理模块，进入组织架构")
    def enter_organization(self):
        self.login_on(username='monica', password='123456')
        self.enter_moudle_name(0)
        time.sleep(1)
        self.operation_child_element(0)

    @allure.step('点击高级查询按钮')
    @allure.description("点击高级查询按钮，展开全部查询条件")
    def click_senior_button(self):
        self.operation_senior_button()
    @allure.step('输入查询条件值')
    @allure.description("操作查询按钮，输入查询条件值")
    def input_search_value(self,index,**kwargs):
        #操作文本输入框
        self.opeation_input_text_query(**kwargs)
        #操作需输入的下拉框
        self.opeation_select_input_query(index)
        #操作有默认值的下拉框
        self.operation_select_default_query(index)
        #点击查询按钮
        self.operation_search_button()

    @allure.step('点击新增按钮（树菜单下拉框封装无法选中值')
    @allure.description("打开新增窗口，新增值")
    def Add_user_data(self):
        pass

    @allure.step('点击添加组织按钮')
    @allure.description("添加组织数据")
    def Add_organization_data(self,*args):
        self.find_element_by_xpath(ADD_ORGANIATION_BUTTON).click()
        self.find_element_by_xpath(ORGANIATION_NAME).send_keys(args[0])

        self.find_element_by_xpath(ORGANIATION_ID).send_keys(args[1])
        time.sleep(1)
        self.operation_confirm_button()


    def main(self):
        self.enter_organization()
        self.Add_organization_data('自动化测试','1234')
        # self.click_senior_button()
        # self.input_search_value(1,search_one='1234',search_two='987654',search_three='15155972770')


if __name__ == '__main__':


    ll = page_one(driver())
    # 'username'='lijie7','password'='123456789'


    ll.main()



    # time.sleep(3)
    # ll.delete_page_screen()
    # aaa = ll.operation_delete()
    # print(aaa)
    # connect_sql.close()
