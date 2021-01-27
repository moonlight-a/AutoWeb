import os,random,time,yaml
from public.base import driver
from Tools.sql_tools import connect_sql
from public.enter_moudle import enter_page
from selenium.webdriver.common.by import By
PATH = os.path.dirname(os.path.dirname(__file__))
data_load = yaml.load(open(PATH + '//Test_data//test_role_data.yaml', 'r', encoding='utf-8'))
query_data = data_load.get('add1_正向')
element_load = yaml.load(open(PATH + '//page_elements//page_element.yaml','r',encoding='utf-8'))
search_load = yaml.load(open(PATH + '//page_elements//search_yaml.yaml','r',encoding='utf-8'))
connect_sql = connect_sql()
'''查询条件元素信息'''
Name_select_js = search_load.get('Name_select_js')
Login_id_element = (By.XPATH,search_load.get('Login_id_element'))
Select_value_element = (By.CLASS_NAME,search_load.get('search_element'))
Job_number_element = (By.XPATH,search_load.get('Job_number_element'))
Phone_element = (By.XPATH,search_load.get('Phone_element'))
Account_status_element =search_load.get('Account_status_js')
Search_button_element = (By.XPATH,search_load.get('search_button_element'))

class page_one(enter_page):

    def screen_page(self):
        self.enter_moudle_name('系统管理')
        time.sleep(2)
        self.get_image('组织架构')
        return None

    #操作高级查询按钮，展开所有查询条件并获取值，数据类型:{属性名：元素}
    def get_page_senior_button_element(self):
        check_data =self.operation_check_senior_button()
        check_data.get('高级查询').click()
        return None

#获取页面查询条件字段值
    def get_page_query_value(self):
        check_value_dict =self.operation_check_button_value()

        return check_value_dict

#操作页面查询字段
    def opeation_select_input_query(self):
        filter_name_data = []
        self.select_block(Name_select_js)
        value = self.find_elements_class(Select_value_element)
        [filter_name_data.append(x) for x in value if x.text != '']
        filter_name_data[0].click()

    def opeation_input_query(self,**kwargs):
        login_id = self.find_element_by_xpath(Login_id_element)
        job_number = self.find_element_by_xpath(Job_number_element)
        phone = self.find_element_by_xpath(Phone_element)
        login_id.send_keys(kwargs.get('login_id'))
        job_number.send_keys(kwargs.get('job_number'))
        phone.send_keys(kwargs.get('phone'))

    def operation_select_default_query(self):
        filter_name_data =[]
        self.select_block(Account_status_element)
        value = self.find_elements_class(Select_value_element)
        [filter_name_data.append(x) for x in value if x.text != '']
        filter_name_data[1].click()
        time.sleep(2)
        self.find_element_by_xpath(Search_button_element).click()









    def operation_page_add_screen(self):
        self.get_page_button_element().get('新增').click()
        time.sleep(2)
        self.get_image('新增角色')
        return None

#按照页面字段名称进行传值
    def operation_page_add(self,**kwargs):
        add_filed_text = self.find_elements_class(element_load.get('page_input_text_element'))
        for i in range(len(add_filed_text)):
            add_filed_text[i].send_keys(kwargs.get('role_name'))

        add_filed_rich_text = self.find_elements_class(element_load.get('rich_text_box_element'))
        add_filed_rich_text[0].send_keys(kwargs.get('rich_text'))

        check_box_value = self.operation_checkbox()
        check_box_value[random.randint(0,len(check_box_value))].click()
        self.get_page_button_element().get('提交').click()
        time.sleep(2)

    # 判断kwargs有值，判断调用alert还是tips_error

        if kwargs.get('role_name')  == ' ':
            print(self.get_tips_error())
        elif kwargs.get('role_name') !='':
            print(self.get_alter_text())
        else:
            print(self.get_tips_error())

#获取删除页面截图
    def delete_page_screen(self):
        #获取页面当前总数据条目
        page_count = connect_sql.single_form_data_sql('t_role')
        self.get_page_button_element().get('删除').click()
        self.get_image('角色管理删除')
        return page_count
#操作页面删除按钮，先获取页面总数据条目，删除后在获取总条目判断数据是否被删除
    def operation_delete(self):
        current_count = self.delete_page_screen()
        self.find_element_class(element_load.get('alert_delete_element')).click()
        delete_count = connect_sql.single_form_data_sql('t_role')
        if current_count == delete_count:
            return True
        else:
            return False


if __name__ == '__main__':


    ll = page_one(driver())
    # 'username'='lijie7','password'='123456789'


    ll.screen_page()
    #
    ll.get_page_senior_button_element()
    ll.get_page_query_value()
    ll.opeation_select_input_query()
    ll.opeation_input_query()
    ll.operation_select_default_query()


    # time.sleep(3)
    # ll.delete_page_screen()
    # aaa = ll.operation_delete()
    # print(aaa)
    # connect_sql.close()
