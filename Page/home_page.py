import time

from public.opertion_element import Element

from public.base import driver


class home_action(Element):

    #获取首页图片
    def compare_image(self):
        time.sleep(9)
        self.get_image()




if __name__ == '__main__':
    hh = home_action(driver(),'http://39.101.216.196/sdr/#/login')

    hh.compare_image()