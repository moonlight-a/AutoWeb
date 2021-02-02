import allure
import pytest
from Page.home_page import home_action
from Page.login_page import login_action
from public.base import driver
class Test_login():

    @allure.title("用户名为空")
    @allure.description("用户名为空")

    def test_01(self):
        aa = login_action(driver())
        aa.log_on(username='', password='123456')
        res =aa.check_login_status()

        assert "请输入登录ID" == res[0]

    # @allure.title("用户名为空")
    # def test_02(self):
    #     res =login_action(driver()).log_on(username='moni1ca', password='123456')
    #
    #     assert "账号或密码有误，请检查后重新输入"== res
    #
    # @allure.title("登录正向")
    # @allure.description("输入正确的用户名及密码")
    # def test_03(self):
    #     res =login_action(driver()).log_on(username='monica', password='123456')
    #     assert True== res


if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])