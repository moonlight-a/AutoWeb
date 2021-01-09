
#封装浏览器操作方法
import os
import datetime
import time

import yaml
from selenium.webdriver.support.select import Select
PATH = os.path.dirname(os.path.dirname(__file__))
open_data = open(PATH + '//page_elements//page_element.yaml','r',encoding='utf-8')
read_data = yaml.load(open_data)

from public import base


class Element():

    def __init__(self,driver):
        self.driver = driver


    def find_element_class(self,loc):

        return self.driver.find_element_by_class_name(loc)

    def find_elements_class(self,loc):
        return self.driver.find_elements_by_class_name(loc)

    def find_element_by_id(self,loc):

        return self.driver.find_element_by_id(loc)

    def find_element_by_xpath(self,loc):
        return self.driver.find_element_by_xpath(loc)

    def send_keys(self,value):
        return  self.driver.send_keys(value)

#获取alert弹窗提示语
    def get_alter_text(self):

        time.sleep(1)
        alert_text  = self.find_element_class(read_data.get('alert_element'))

        return alert_text.text
#获取tips提示语
    def get_tips_error(self):
        #由于文本框存在多个值需将错误提示语封装到list
        list_error = []

        error_text = self.find_elements_class(read_data.get('tips_element'))

        if len(error_text) > 1:
            for text in range(len(error_text)):
                list_error.append(error_text[text].text)
            return list_error
        else:
            return error_text[0].text

#截图操作
    def get_image(self,pagename):
        path = os.path.dirname(os.path.dirname(__file__))
        current_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(current_time, '%Y-%m-%d_%H-%M-%S')
        image_file = path + '//Picture//'  + pagename + '_' +time_str + '.png'

        try:

            self.driver.get_screenshot_as_file(image_file)

        except BaseException as e:
            print(e)



#操作下拉框获取下拉框中值
    def get_select_data(self):
        select_list =[]
        #点击下拉康
        self.find_element_class(read_data.get('select_element')).click()
        time.sleep(1)
        select_value = self.find_elements_class(read_data.get('select_value_element'))

        for i in range(len(select_value)):
           select_list.append( select_value[i].text)
        return list

#选中下拉框中的值
    def select_value(self):
        self.find_element_class(read_data.get('select_element')).click()
        time.sleep(1)
        select_value = self.find_elements_class(read_data.get('select_value_element'))[1]
        select_value.click()

        return None

#获取左侧菜单栏数据
    def get_menu_tree(self):

        tree_data = self.find_elements_class(read_data.get('menu_tree_element'))


        return tree_data

#操作数菜单的下拉按钮并获取子级数据
    def tree_button_value(self):
        #将父级节点做为字典key，子级数据以列表形式进行存储，示例：‘系统管理’：[1,2,3]
        dict= {}
        child_tree = read_data.get(('menu_tree_value_element'))
        for menu_i in range(len(self.get_menu_tree())):
            self.get_menu_tree()[menu_i].click()

            child_tree_data = self.find_elements_class(child_tree)

            child_list = []
            for child_i in range(len(child_tree_data)):

                if child_tree_data[child_i].text !='':
                    child_list.append(child_tree_data[child_i].text)

            dict[self.get_menu_tree()[menu_i].text] = child_list
        return dict

#操作数菜单的下拉按钮并获取子级元素
    def tree_button_element(self):
        #将父级节点做为字典key，子级数据以列表形式进行存储，示例：‘系统管理’：[1,2,3]
        dict= {}
        child_tree = read_data.get(('menu_tree_value_element'))
        for menu_i in range(len(self.get_menu_tree())):
            self.get_menu_tree()[menu_i].click()

            child_tree_data = self.find_elements_class(child_tree)

            child_list = []
            time.sleep(2)
            for child_i in range(len(child_tree_data)):

                if child_tree_data[child_i].text !='':
                    child_list.append(child_tree_data[child_i])

            dict[self.get_menu_tree()[menu_i].text] = child_list
        return dict

#获取页面操作按钮对应的元素，返回数据类型：‘按钮名称’:'元素名称'
    def operation_button(self):
        dict ={}
        button_list = self.find_elements_class(read_data.get('operation_button_element'))
        for i in range(len(button_list)):
            dict[button_list[i].text] = button_list[i]
        return dict
#获取查询结果页面返回的数量值
    def get_query_data_total(self):
        total = self.find_element_class(read_data.get('query_result_count'))
        total_value = total.text
        str_list = total_value.split(' ')
        int_value = str_list[1]
        return int_value

# 操作复选框按钮
    def operation_checkbox(self):
        check_box = self.find_elements_class(read_data.get('check_box_element'))
        check_box_list = [check_box[i] for i in range(len(check_box))]

        return check_box_list
        pass


#操作页面删除按钮
    def operation(self):
        pass

#获取页面查询条件字段值
    def get_query_value(self):
        list =[]
        query_list = self.find_elements_class(read_data.get('query_value_element'))
        for query_value in range(len(query_list)):
            list.append(query_list[query_value].text)

        return list

if __name__ == '__main__':

    e = Element(base.driver())
    w = e.get_alter_text()
    print(w)