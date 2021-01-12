import os,random,time,yaml

from Page.login_page import login_action
from public.base import driver
from Tools.sql_tools import connect_sql
from public.opertion_element import Element

PATH = os.path.dirname(os.path.dirname(__file__))
data_load = yaml.load(open(PATH + '//Test_data//test_role_data.yaml', 'r', encoding='utf-8'))
query_data = data_load.get('add1_正向')
element_load = yaml.load(open(PATH + '//page_elements//page_element.yaml','r',encoding='utf-8'))
connect_sql = connect_sql()

class page_one(login_action):



    def enter_page_one(self):
        #先获取每个父级树菜单中对应的自己元素，在操作父级值
        child_element = self.tree_button_element()

        tree_data = self.get_menu_tree()

        tree_data[0].click()
        time.sleep(2)
        list_child = child_element.get('系统管理')
        list_child[0].click()


    def screen_page(self):
        self.get_image('角色管理')
        return None

    def get_page_button_element(self):
        button_dict = self.operation_button()
        return button_dict

#获取页面查询条件字段值
    def get_page_query_value(self):

        self.get_query_value()

        return None

#操作页面查询功能,通过查询条件获取查询结果条目，并进行判断
    def opeation_page_query(self,value):

        query_text = self.find_element_class(element_load.get('page_input_text_element'))
        query_element = self.get_page_button_element().get('查询')
        query_text.send_keys(value)
        time.sleep(2)
        query_element.click()
        time.sleep(2)

        if self.get_query_data_total() == connect_sql.signle_form_sql(form_name='t_role',field_name='name',value=value):
            return True
        else:
            return False

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
    ll.log_on(username= 'monica',password = '123456')

    ll.enter_page_one()
    # time.sleep(3)
    # ll.delete_page_screen()
    # aaa = ll.operation_delete()
    # print(aaa)
    # connect_sql.close()
