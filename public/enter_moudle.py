import time

from Page.login_page import login_action
from public.base import driver

class enter_page(login_action):

    def enter_moudle_name(self):
        #self.log_on(username='15155972770',password='123456')
        self.log_on(username='monica', password='123456')
        # 先获取每个父级树菜单中对应的自己元素，在操作父级值
        www = self.get_menu_tree()
        www[0].click()
        time.sleep(4)
        www[1].click()
        time.sleep(4)
        www[2].click()
        time.sleep(4)
        www[3].click()
        time.sleep(4)
        www[4].click()
        time.sleep(4)
        www[5].click()
        time.sleep(4)
        www[6].click()
        # child_element = self.tree_button_element()
        #
        # tree_data = self.get_menu_tree()
        #
        #
        # tree_data[0].click()
        # time.sleep(2)
        # list_child = child_element.get(moudle_name)
        # list_child[0].click()

if __name__ == '__main__':

    enter_pag = enter_page(driver())

    enter_pag.enter_moudle_name()