from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.wait import WebDriverWait

from public.base import driver
#封装浏览器操作方法

class Element():

    def __init__(self,driver,url):
        self.driver = driver
        self.url = url
        self.open()

    def open(self):
        url = self.url
        self.driver.get(url)

    def find_element_class(self,loc):

        return self.driver.find_element_by_class_name(loc)

    def find_elements_class(self,loc):
        return self.driver.find_element_by_class_name(loc)

    def find_element_by_id(self,loc):

        return self.driver.find_element_by_id(loc)

    def find_element_by_xpath(self,loc):
        return self.driver.find_element_by_xpath(loc)


e = Element(driver(),'http://39.101.216.196/sdr/#/login')
w = e.find_element('el-input__inner')
print(w)