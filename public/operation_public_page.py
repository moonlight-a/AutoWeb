#封装页面操作的公共方法
import os,time,yaml
from selenium.webdriver.common.by import By

from public.base import driver
from public.opertion_element import Element
PATH = os.path.dirname(os.path.dirname(__file__))
page_public_element = yaml.load(open(PATH + '//page_elements//page_public_element.yaml','r',encoding='utf-8'))

Alert_element = (By.CLASS_NAME,page_public_element.get('alert_element'))
Tips_element = (By.CLASS_NAME,page_public_element.get('tips_element'))
Select_element = (By.CLASS_NAME,page_public_element.get('select_element'))
Select_value_element = (By.CLASS_NAME,page_public_element.get('select_value_element'))
Menu_tree_element = (By.XPATH,page_public_element.get('menu_tree_element'))
Menu_tree_value_element = (By.CLASS_NAME,page_public_element.get('menu_tree_value_element'))
Check_senior_button_element = (By.CLASS_NAME,page_public_element.get('check_senior_button_element'))
Operation_button_element = (By.CLASS_NAME,page_public_element.get('operation_button_element'))
Query_result_count_element = (By.CLASS_NAME,page_public_element.get('query_result_count'))
Check_box_element = (By.CLASS_NAME,page_public_element.get('check_box_element'))
Query_value_element = (By.CLASS_NAME,page_public_element.get('query_value_element'))
Child_data_element = (By.CLASS_NAME,"Child_data_element")
Name_select_js = page_public_element.get('Name_select_js')
Search_id_element = (By.XPATH,page_public_element.get('Search_id_element'))
# Select_value_element = (By.CLASS_NAME,page_public_element.get('Search_element'))
Search_Job_number_element = (By.XPATH,page_public_element.get('Search_Job_number_element'))
Search_Phone_element = (By.XPATH,page_public_element.get('Search_Phone_element'))
Defaule_select_value_js =page_public_element.get('Defaule_select_value_js')
Search_button_element = (By.XPATH,page_public_element.get('Search_button_element'))
Clear_button_element = (By.XPATH,page_public_element.get('Clear_buttion_element'))
Senior_button_element = (By.XPATH,page_public_element.get('Senior_button_element'))
Put_senior_button_element = (By.XPATH,page_public_element.get('Put_senior_button_element'))
Add_button_element = (By.XPATH,page_public_element.get('Add_button_element'))
Import_button_element = (By.XPATH,page_public_element.get('Import_button_element'))
Download_button_element = (By.XPATH,page_public_element.get('Download_button_element'))

Check_all_button_element = (By.CLASS_NAME,page_public_element.get('checkbox_button_element'))
Add_organization_element = (By.XPATH,page_public_element.get('Add_organization_element'))
'''元素信息end'''

class operation_page_function(Element):
    #操作checkbox按钮
    def operation_checkbox(self):
        self.find_element_by_xpath(Check_all_button_element).click()

    # 操作新增按钮，打开新增窗口后传入新增值
    def operation_add_button(self):
        self.find_element_by_xpath(Add_button_element).click()

    # 操作页面高级查询按钮展开所有查询条件
    def operation_senior_button(self):
        self.find_element_by_xpath(Senior_button_element).click()

    # 操作页面可查询下拉框元素
    def opeation_select_input_query(self):
        filter_name_data = []
        self.select_block(Name_select_js)
        value = self.find_elements_class(Select_value_element)
        [filter_name_data.append(x) for x in value if x.text != '']
        filter_name_data[0].click()

    # 操作查询条件文本输入框（根据查询条件值需要进行修改,字典key根据search_one,规则递增）
    def opeation_input_query(self, **kwargs):
        search_value_one = self.find_element_by_xpath(Search_id_element)
        search_value_two = self.find_element_by_xpath(Search_Job_number_element)
        search_value_thr = self.find_element_by_xpath(Search_Phone_element)
        search_value_one.send_keys(kwargs.get('search_one'))
        search_value_two.send_keys(kwargs.get('search_two'))
        search_value_thr.send_keys(kwargs.get('search_three'))

    # 操作默认值的下拉框,并默认选择下标为1的数据
    def operation_select_default_query(self):
        filter_name_data = []
        self.select_block(Defaule_select_value_js)
        value = self.find_elements_class(Select_value_element)
        [filter_name_data.append(x) for x in value if x.text != '']
        filter_name_data[1].click()

    # 操作页面查询按钮
    def operation_search_button(self):
        self.find_element_by_xpath(Search_button_element).click()

    # 操作页面清空按钮
    def operation_clean_button(self):
        self.find_element_by_xpath(Clear_button_element).click()

    # def search_input_text(self):
    #     input_text = self.find_elements_class(element_load.get('input_text_element'))
    #     return input_text
    #
    #
    # def search_select(self):
    #     filter_data = []
    #     select_value = self.find_elements_class(element_load.get('check_select_value_element'))
    #     [filter_data.append(x) for x in select_value if x.text != '']
    #     return filter_data
    #获取子级元素的数据，并通过下标去点击进行操作
    def operation_child_element(self):
        child_list_data = self.find_elements_class()
        print(child_list_data[1].click())

    #进入对应的页面模块
    def enter_moudle_name(self,index):
        # 先获取每个父级树菜单中对应的自己元素，在操作父级值
        return self.get_menu_tree()[index].click()

    # 通过js属性操作下拉框是隐藏属性可见
    def select_block(self, js):

        self.driver.execute_script(js)

    # 获取alert弹窗提示语
    def get_alter_text(self):
        alert_text = self.find_element_class(Alert_element)
        return alert_text.text

    # 获取tips提示语
    def get_tips_error(self):
        # 由于文本框存在多个值需将错误提示语封装到list
        list_error = []
        error_text = self.find_elements_class(Tips_element)
        for text in range(len(error_text)):
            list_error.append(error_text[text].text)
        return list_error
    # 操作下拉框获取下拉框中值,通过传入的下标，选择值
    def get_select_data(self,index):
        select_list = []
        # 点击下拉框
        self.find_element_class(Select_element).click()
        time.sleep(1)
        select_value = self.find_elements_class(Select_value_element)

        for i in range(len(select_value)):
            select_list.append(select_value[i].text)
        return select_list[index]

    # # 选中下拉框中的值
    # def select_value(self):
    #     self.find_element_class(Select_element).click()
    #     time.sleep(1)
    #     select_value = self.find_elements_class(Select_value_element)[1]
    #     select_value.click()
    #
    #     return None

    # 获取左侧菜单栏数据
    def get_menu_tree(self):
        tree_data = self.find_elements_by_xpath(Menu_tree_element)
        return tree_data

    # # 操作数菜单的下拉按钮并获取子级数据
    # def tree_button_value(self):
    #     # 将父级节点做为字典key，子级数据以列表形式进行存储，示例：‘系统管理’：[1,2,3]
    #     dict = {}
    #     child_tree = Menu_tree_value_element
    #     for menu_i in range(len(self.get_menu_tree())):
    #         self.get_menu_tree()[menu_i].click()
    #
    #         child_tree_data = self.find_elements_class(child_tree)
    #
    #         child_list = []
    #         for child_i in range(len(child_tree_data)):
    #
    #             if child_tree_data[child_i].text != '':
    #                 child_list.append(child_tree_data[child_i].text)
    #
    #         dict[self.get_menu_tree()[menu_i].text] = child_list
    #     return dict



    # # 查询条件存在高级查询的页面先操作高级查询按钮展开所有查询条件，在返回数据，数据类型：{查询字段：元素}
    # def operation_check_senior_button(self):
    #     senior_check_data_dict = {}
    #     # 获取高级查询元素
    #     senior_element = self.find_elements_class(Check_senior_button_element)
    #     time.sleep(1)
    #     for i in range(len(senior_element)):
    #         senior_check_data_dict[senior_element[i].text] = senior_element[i]
    #
    #     return senior_check_data_dict

    # # 获取查询条件字段值
    # def operation_check_button_value(self):
    #
    #     check_data_dict = {}
    #     # 获取高级查询元素
    #     senior_element = self.find_elements_class(Operation_button_element)
    #     time.sleep(1)
    #     for i in range(len(senior_element)):
    #         replace_str = str(senior_element[i].text).replace('：', '')
    #         check_data_dict[replace_str] = senior_element[i]
    #
    #     return check_data_dict

    # 获取查询结果页面返回的数量值
    def get_query_data_total(self):
        total = self.find_element_class(Query_result_count_element)
        total_value = total.text
        str_list = total_value.split(' ')
        int_value = str_list[1]
        return int_value

    # # 操作复选框按钮
    # def operation_checkbox(self):
    #     check_box = self.find_elements_class(Check_box_element)
    #     check_box_list = [check_box[i] for i in range(len(check_box))]
    #
    #     return check_box_list

    # # 获取页面查询条件字段值
    # def get_query_value(self):
    #     list = []
    #     query_list = self.find_elements_class(Query_value_element)
    #     for query_value in range(len(query_list)):
    #         list.append(query_list[query_value].text)
    #
    #     return list
if __name__ == '__main__':
    operation_page = operation_page_function(driver())

    operation_page.enter_moudle_name(1)