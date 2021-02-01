
#封装浏览器操作方法
import os
import datetime
import time
import yaml
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public import base
PATH = os.path.dirname(os.path.dirname(__file__))
open_data = open(PATH + '//page_elements//page_public_element.yaml','r',encoding='utf-8')
read_data = yaml.load(open_data)

Alert_element = (By.CLASS_NAME,read_data.get('alert_element'))
Tips_element = (By.CLASS_NAME,read_data.get('tips_element'))
Select_element = (By.CLASS_NAME,read_data.get('select_element'))
Select_value_element = (By.CLASS_NAME,read_data.get('select_value_element'))
Menu_tree_element = (By.XPATH,read_data.get('menu_tree_element'))
Menu_tree_value_element = (By.CLASS_NAME,read_data.get('menu_tree_value_element'))
Check_senior_button_element = (By.CLASS_NAME,read_data.get('check_senior_button_element'))
Operation_button_element = (By.CLASS_NAME,read_data.get('operation_button_element'))
Query_result_count_element = (By.CLASS_NAME,read_data.get('query_result_count'))
Check_box_element = (By.CLASS_NAME,read_data.get('check_box_element'))
Query_value_element = (By.CLASS_NAME,read_data.get('query_value_element'))

class Element():

    def __init__(self,driver):
        self.driver = driver


    def find_element_class(self,*loc):
        element = WebDriverWait(self.driver,5,0.5).until(
            EC.presence_of_element_located(*loc))
        return element

    def find_elements_class(self,*loc):
        element = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_all_elements_located(*loc))
        return element

    def find_element_by_id(self,*loc):
        element = WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located(*loc))
        return element

    def find_element_by_xpath(self,*loc):
        element = WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located(*loc))
        return element

    def find_elements_by_xpath(self,*loc):
        element = WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_all_elements_located(*loc))
        return element

    def find_element_by_link_text(self,*loc):
        link_text_element = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(*loc))
        return link_text_element

  #发送文字
    def send_keys(self,value):
        return  self.driver.send_keys(value)

#获取alert弹窗提示语
    def get_alter_text(self):
        alert_text  = self.find_element_class(Alert_element)
        return alert_text.text
#获取tips提示语
    def get_tips_error(self):
        #由于文本框存在多个值需将错误提示语封装到list
        list_error = []
        error_text = self.find_elements_class(Tips_element)

        if len(error_text) > 1:
            for text in range(len(error_text)):
                list_error.append(error_text[text].text)
            return list_error
        else:
            return error_text[0].text
# 获取页面当前url
    def get_currernt_url(self):


        return self.driver.current_url

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

#通过js属性操作下拉框是隐藏属性可见
    def select_block(self,js):

        # js = 'document.querySelectorAll("select")[0].style.display="block";'
        self.driver.execute_script(js)


#操作下拉框获取下拉框中值
    def get_select_data(self):
        select_list =[]
        #点击下拉框
        self.find_element_class(Select_element).click()
        time.sleep(1)
        select_value = self.find_elements_class(Select_value_element)

        for i in range(len(select_value)):
           select_list.append( select_value[i].text)
        return list

# 选中下拉框中的值
    def select_value(self):
        self.find_element_class(Select_element).click()
        time.sleep(1)
        select_value = self.find_elements_class(Select_value_element)[1]
        select_value.click()

        return None

#获取左侧菜单栏数据
    def get_menu_tree(self):
        tree_data = self.find_elements_by_xpath(Menu_tree_element)
        return tree_data

#操作数菜单的下拉按钮并获取子级数据
    def tree_button_value(self):
        #将父级节点做为字典key，子级数据以列表形式进行存储，示例：‘系统管理’：[1,2,3]
        dict= {}
        child_tree = Menu_tree_value_element
        for menu_i in range(len(self.get_menu_tree())):
            self.get_menu_tree()[menu_i].click()

            child_tree_data = self.find_elements_class(child_tree)

            child_list = []
            for child_i in range(len(child_tree_data)):

                if child_tree_data[child_i].text !='':
                    child_list.append(child_tree_data[child_i].text)

            dict[self.get_menu_tree()[menu_i].text] = child_list
        return dict

# 操作数菜单的下拉按钮并获取子级元素
    def tree_button_element(self):
        #将父级节点做为字典key，子级数据以列表形式进行存储，示例：‘系统管理’：[1,2,3]
        dict= {}
        child_tree = Menu_tree_value_element
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
    # 查询条件存在高级查询的页面先操作高级查询按钮展开所有查询条件，在返回数据，数据类型：{查询字段：元素}
    def operation_check_senior_button(self):
        senior_check_data_dict ={}
        #获取高级查询元素
        senior_element = self.find_elements_class(Check_senior_button_element)
        time.sleep(1)
        for i in range(len(senior_element)):
            senior_check_data_dict[senior_element[i].text] = senior_element[i]



        return senior_check_data_dict
    #获取查询条件字段值
    def operation_check_button_value(self):

        check_data_dict ={}
        #获取高级查询元素
        senior_element = self.find_elements_class(Operation_button_element)
        time.sleep(1)
        for i in range(len(senior_element)):
            replace_str = str(senior_element[i].text).replace('：','')
            check_data_dict[replace_str] = senior_element[i]



        return check_data_dict

#获取查询结果页面返回的数量值
    def get_query_data_total(self):
        total = self.find_element_class(Query_result_count_element)
        total_value = total.text
        str_list = total_value.split(' ')
        int_value = str_list[1]
        return int_value

# 操作复选框按钮
    def operation_checkbox(self):
        check_box = self.find_elements_class(Check_box_element)
        check_box_list = [check_box[i] for i in range(len(check_box))]

        return check_box_list
        pass


#操作页面删除按钮
    def operation(self):
        pass

#获取页面查询条件字段值
    def get_query_value(self):
        list =[]
        query_list = self.find_elements_class(Query_value_element)
        for query_value in range(len(query_list)):
            list.append(query_list[query_value].text)

        return list
#操作需要鼠标悬浮显示元素值
    def mouse_action(self,value_text,operation_text):
        ActionChains(self.driver).move_to_element(self.find_element_by_link_text(value_text)).perform()
        time.sleep(2)
        self.find_element_by_link_text(operation_text).click()
if __name__ == '__main__':

    e = Element(base.driver())
    w = e.tree_button_element()
    print(w)