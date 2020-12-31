import time

from public.opertion_element import Element

from public.base import driver


class home_action(Element):

    #首页只需要判断页面是否与本地图片一致
    def compare_image(self):
        time.sleep(9)
        self.get_image()




if __name__ == '__main__':
    hh = home_action(driver(),'http://39.101.216.196/sdr/#/login')

    hh.compare_image()