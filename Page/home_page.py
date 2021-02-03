import time
from public.base import driver
from public.operation_public_page import operation_page_function



class home_action(operation_page_function):

    #获取首页图片
    def compare_image(self):
        time.sleep(3)
        self.get_image('首页')




if __name__ == '__main__':
    hh = home_action(driver())

    hh.compare_image()