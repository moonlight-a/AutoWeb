# import os,time,yaml
# from public.base import driver
# from Tools.sql_tools import connect_sql
# from selenium.webdriver.common.by import By
# from public.enter_moudle import enter_page
# from public.opertion_element import Element
#
# PATH = os.path.dirname(os.path.dirname(__file__))
# # organization_load = yaml.load(open(PATH + '//page_elements//page_function_yaml.yaml','r',encoding='utf-8'))
# organization_load = yaml.load(open(PATH + '//page_elements//page_organization_element.yaml','r',encoding='utf-8'))
# connect_sql = connect_sql()
# '''元素信息start'''
# Name_select_js = organization_load.get('Name_select_js')
# Login_id_element = (By.XPATH,organization_load.get('Login_id_element'))
# Select_value_element = (By.CLASS_NAME,organization_load.get('Search_element'))
# Job_number_element = (By.XPATH,organization_load.get('Job_number_element'))
# Phone_element = (By.XPATH,organization_load.get('Phone_element'))
# Account_status_element =organization_load.get('Account_status_js')
# Search_button_element = (By.XPATH,organization_load.get('Search_button_element'))
# Clear_button_element = (By.XPATH,organization_load.get('Clear_buttion_element'))
# Senior_button_element = (By.XPATH,organization_load.get('Senior_button_element'))
# Put_senior_button_element = (By.XPATH,organization_load.get('Put_senior_button_element'))
# Add_button_element = (By.XPATH,organization_load.get('Add_button_element'))
# Import_button_element = (By.XPATH,organization_load.get('Import_button_element'))
# Download_button_element = (By.XPATH,organization_load.get('Download_button_element'))
# Select_add_organization_element = (By.XPATH,organization_load.get('Select_add_organization_element'))
# Select_add_value_elenment = (By.XPATH,organization_load.get('Select_add_value_elenment'))
# Select_add_role_element = (By.XPATH,organization_load.get('Select_add_role_element'))
# Add_Login_id_element = (By.XPATH,organization_load.get('Add_Login_id_element'))
# Add_name_element = (By.XPATH,organization_load.get('Add_name_element'))
# Add_Job_number_element = (By.XPATH,organization_load.get('Add_Job_number_element'))
# Add_Phone_element = (By.XPATH,organization_load.get('Add_Phone_element'))
# Add_Position_element = (By.XPATH,organization_load.get('Add_Position_element'))
# Add_Email_element = (By.XPATH,organization_load.get('Add_Email_element'))
# wwwwwwww = (By.XPATH,organization_load.get('organization_test_element'))
# Check_all_button_element = (By.CLASS_NAME,organization_load.get('checkbox_button_element'))
# Add_organization_element = (By.XPATH,organization_load.get('Add_organization_element'))
# '''元素信息end'''
#
# class operation_function_page(enter_page):
#     def screen_page(self):
#         self.enter_moudle_name()
#         self.find_element_by_xpath(wwwwwwww).click()
#         time.sleep(2)
#         self.get_image('组织架构')
#         return None
# #
# #操作页面高级查询按钮展开所有查询条件
#     def operation_senior_button(self):
#         self.find_element_by_xpath(Senior_button_element).click()
# #操作页面可查询下拉框元素
#     def opeation_select_input_query(self):
#         filter_name_data = []
#         self.select_block(Name_select_js)
#         value = self.find_elements_class(Select_value_element)
#         [filter_name_data.append(x) for x in value if x.text != '']
#         filter_name_data[0].click()
# # #操作页面文本输入框
# #     def opeation_input_query(self,**kwargs):
# #         login_id = self.find_element_by_xpath(Login_id_element)
# #         job_number = self.find_element_by_xpath(Job_number_element)
# #         phone = self.find_element_by_xpath(Phone_element)
# #         login_id.send_keys(kwargs.get('login_id'))
# #         job_number.send_keys(kwargs.get('job_number'))
# #         phone.send_keys(kwargs.get('phone'))
# #
# # #操作页面有默认值的下拉框
# #     def operation_select_default_query(self):
# #         filter_name_data =[]
# #         self.select_block(Account_status_element)
# #         value = self.find_elements_class(Select_value_element)
# #         [filter_name_data.append(x) for x in value if x.text != '']
# #         filter_name_data[1].click()
# #
# # #操作页面查询按钮
# #     def operation_search_button(self):
# #         self.find_element_by_xpath(Search_button_element).click()
# #
# # #操作页面清空按钮
# #     def operation_clean_button(self):
# #         self.find_element_by_xpath(Clear_button_element).click()
#
# #操作数据库验证查询结果与数据库查询结果是否一致
#     def operation_sql_result(self):
#         pass
#
#
# # #操作新增按钮，打开新增窗口后传入新增值
# #     def operation_add_button(self):
# #         self.find_element_by_xpath(Add_button_element).click()
# #操作新增模块中，文本框输入
#     def operation_add_input_text(self,**kwargs):
#         Add_Login_id = self.find_element_by_xpath(Add_Login_id_element)
#         Add_name = self.find_element_by_xpath(Add_name_element)
#         Add_Job_number = self.find_element_by_xpath(Add_Job_number_element)
#         Add_Phone = self.find_element_by_xpath(Add_Phone_element)
#         Add_Position = self.find_element_by_xpath(Add_Position_element)
#         Add_Email = self.find_element_by_xpath(Add_Email_element)
#         Add_name.send_keys(kwargs.get('Add_name'))
#         Add_Login_id.send_keys(kwargs.get('Add_Login'))
#         Add_Position.send_keys(kwargs.get('Add_Position'))
#         Add_Job_number.send_keys(kwargs.get('Add_Job'))
#         Add_Phone.send_keys(kwargs.get('Add_Phone'))
#         Add_Email.send_keys(kwargs.get('Add_Email'))
#
#     ###该下拉框外层数被封装无法通过元素去调用#######
#     def operation_add_select(self):
#         filter_name_data =[]
#         organization_select = self.find_elements_by_xpath(Select_add_organization_element)
#         organization_select[4].click()
#
#         www= self.find_element_by_xpath(Select_add_value_elenment)
#         print(www)
#
#     ###该下拉框外层数被封装无法通过元素去调用#######
#
#     def operation_checkbox(self):
#         self.find_element_by_xpath(Check_all_button_element).click()
#
#         pass
#
#
#
#         # data_value = self.find_elements_class(Select_add_value_elenment)
#         # [filter_name_data.append(x) for x in data_value if x.text != '']
#         # filter_name_data[1].click()
#
#         pass
#
#     #操作添加组织按钮
#     def operation_add_organization(self):
#         self.find_element_by_xpath(Add_organization_element).click()
#
#
#     def main(self):
#         self.screen_page()
#         self.operation_add_organization()
#         # self.operation_add_button()
#         # self.operation_add_input_text(Add_name='selnina',Add_Login='monica',Add_Position='测试',Add_Job='123456',Add_Phone='15155972770',Add_Email='563455843@qq.com')
#         # self.operation_add_select()
#         # self.operation_senior_button()
#         # self.opeation_select_input_query()
#         # self.opeation_input_query(login_id='ceshi',job_number='1234',phone='15155972777')
#         # self.operation_select_default_query()
#         # self.operation_search_button()
#         # time.sleep(3)
#         # self.operation_clean_button()
#
# if __name__ == '__main__':
#
#
#     ll = search_page(driver())
#     # 'username'='lijie7','password'='123456789'
#
#
#     ll.main()
#
#     # time.sleep(3)
#     # ll.delete_page_screen()
#     # aaa = ll.operation_delete()
#     # print(aaa)
#     # connect_sql.close()
