import os,time,yaml, allure
from Page.login_page import login_action
from public.base import driver

from selenium.webdriver.common.by import By
PATH = os.path.dirname(os.path.dirname(__file__))
organ_framework = yaml.load(open(PATH + '//page_elements//page_organization_element.yaml','r',encoding='utf-8'))
public_element = yaml.load(open(PATH + '//page_elements//page_public_element.yaml','r',encoding='utf-8'))

#添加组织
ADD_ORGANIATION_BUTTON = (By.XPATH,organ_framework.get('Add_organization_element'))
#组织名称
ORGANIATION_NAME = (By.XPATH,organ_framework.get('Add_organization_name_element'))
#组织编号
ORGANIATION_ID = (By.XPATH,organ_framework.get('Add_organization_id_element'))
#组织确定提交按钮
ADD_ORGANIATION_CONFIRM_BUTTON = (By.XPATH,organ_framework.get('Add_organization_confirm_element'))
#新增编辑窗口确定按钮下标（32）
CONFIRM_BUTTON = (By.XPATH,organ_framework.get('Confirm_button_element'))
#新增编辑窗口取消按钮下标（32）
CLEAR_BUTTON = (By.XPATH,organ_framework.get('Clear_button_element'))
#新增编辑窗口确定并继续创建按钮，下标（1）
CONFIRM_CONTINUE_BUTTON = (By.XPATH,organ_framework.get('Confirm&continue_button_element'))
#添加子组织元素，下标（0）
ADD_CHILD_ORGANIZATION_BUTTON = (By.XPATH,organ_framework.get('Confirm&continue_button_element'))
#下载导入按钮
DOWNLOAD_BUTTON = (By.XPATH,public_element.get('Download_button_element'))
#操作左侧添加组织数据隐藏数据
Select_dropdown_js = public_element.get('Select_dropdown')
#添加组织左侧数据元素
LeftTree_organization_element = (By.CLASS_NAME,organ_framework.get('LeftTree_organization_element'))
#添加组织左侧数据更多按钮
Hide_data = (By.CLASS_NAME,organ_framework.get('Hide_data_element'))
class page_one(login_action):

    @allure.step('进入系统首页')
    @allure.description("点击页面系统管理模块，进入组织架构")
    def enter_organization(self):
        # self.login_on(username='monica', password='123456')
        self.login_on(username='15155972770', password='123456')
        self.enter_moudle_name(1)
        time.sleep(1)
        self.operation_child_element(0)

    @allure.step('点击高级查询按钮')
    @allure.description("点击高级查询按钮，展开全部查询条件")
    def click_senior_button(self):
        self.operation_senior_button()

    @allure.step('输入查询条件值')
    @allure.description("操作查询按钮，输入查询条件值")
    def input_search_value(self,index,**kwargs):
        #操作文本输入框
        self.opeation_input_text_query(**kwargs)
        #操作需输入的下拉框
        self.opeation_select_input_query(index)
        #操作有默认值的下拉框
        self.operation_select_default_query(index)
        #点击查询按钮
        self.operation_search_button()

    @allure.step('点击新增按钮（树菜单下拉框封装无法选中值')
    @allure.description("打开新增窗口，新增值")
    def Add_user_data(self):
        pass

    @allure.step('点击添加组织按钮,并进行提交')
    @allure.description("添加组织数据")
    def Add_organization_data(self,*args):
        self.find_element_by_xpath(ADD_ORGANIATION_BUTTON).click()
        self.find_element_by_xpath(ORGANIATION_NAME).send_keys(args[0])
        self.find_element_by_xpath(ORGANIATION_ID).send_keys(args[1])
        value = self.find_elements_by_xpath(CONFIRM_BUTTON)
        value[32].click()

    @allure.step('点击添加组织按钮,并点击取消按钮')
    @allure.description("取消添加组织数据")
    def cancel_organization_data(self):
        self.find_element_by_xpath(ADD_ORGANIATION_BUTTON).click()
        value = self.find_elements_by_xpath(CLEAR_BUTTON)
        value[32].click()



    @allure.step('操作导入按钮，并通过文件路径获取导入的文件')
    @allure.description("获取本地文件路径，并导入文件")
    #导入文件
    def operation_import(self,file_path):
        self.operation_import_button(file_path)
    @allure.step('操作下载导入按钮')
    @allure.description("点击下载导入按钮")
    #下载导入文件按钮
    def operation_download_button(self):
        self.find_element_by_xpath(DOWNLOAD_BUTTON).click()

    @allure.step("操作左侧树,通过js操作隐藏属性，获取隐藏属性值进行数据封装")
    #获取左侧树隐藏属性数据，并封装成dict，示例：{“属性中文名称”:元素属性}
    def operation_hide_data(self):
        dict={}
        data_list=[]
        self.select_block(Select_dropdown_js)
        self.find_element_class(LeftTree_organization_element).click()
        hide_data = self.find_elements_class(Hide_data)
        #隐藏属性只有四条数据，故通过切片进行截取
        [data_list.append(hide_data[i]) for i in range(len(hide_data[0:4]))]
        for i in range(len(data_list)):
            dict[data_list[i].text] = data_list[i]
        return dict
    @allure.step('添加子组织数据')
    def operation_add_child_organization(self,*args):
        self.operation_hide_data().get('添加子组织').click()
        self.find_element_by_xpath(ORGANIATION_NAME).send_keys(args[0])
        self.find_element_by_xpath(ORGANIATION_ID).send_keys(args[1])
        value = self.find_elements_by_xpath(CONFIRM_BUTTON)
        value[32].click()
        return None
    @allure.step('删除组织数据')
    def operation_delete_organization(self):
        self.operation_hide_data().get('删除').click()
        #删除操作会进行二次确认需调用操作二次弹窗方法
        self.operation_second_cancle_button(5)



    def main(self):
        self.enter_organization()
        time.sleep(3)
        self.operation_hide_data()
        self.operation_delete_organization()

        # self.click_senior_button()
        # self.input_search_value(1,search_one='1234',search_two='987654',search_three='15155972770')


if __name__ == '__main__':


    ll = page_one(driver())
    # 'username'='lijie7','password'='123456789'


    ll.main()



    # time.sleep(3)
    # ll.delete_page_screen()
    # aaa = ll.operation_delete()
    # print(aaa)
    # connect_sql.close()
