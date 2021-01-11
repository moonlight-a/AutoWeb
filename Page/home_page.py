import time

from Page.login_page import login_action

from public.base import driver


class home_action(login_action):

    #获取首页图片
    def compare_image(self):
        time.sleep(3)
        self.get_image('首页')




if __name__ == '__main__':
    hh = home_action(driver())

    hh.compare_image()