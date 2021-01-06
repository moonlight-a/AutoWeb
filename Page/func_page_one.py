import time

from Page.login_page import login_action
from public.base import driver


class page_one(login_action):


    def operation_page_one_screen(self):
        #先获取每个父级树菜单中对应的自己元素，在操作父级值
        child_element = self.tree_button_element()
        tree_data = self.get_menu_tree()

        tree_data[0].click()
        time.sleep(2)
        list_child = child_element.get('系统管理')
        list_child[0].click()
        #点击页面第一条数据后，进行截图
        time.sleep(2)
        self.get_image('系统管理')

    def opeation_page_query(self,value):
        pass


    def operation_page_add(self,**kwargs):
        pass






if __name__ == '__main__':


    ll = page_one(driver())
    # 'username'='lijie7','password'='123456789'
    ll.log_on(username= 'lijie7',password = '12345678')

    ll.operation_page_one_screen()