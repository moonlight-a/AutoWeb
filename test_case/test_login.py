import allure
import pytest

from Page.login_page import login_action
from public.base import driver


class Test_login():
    @pytest.mark.xfail
    @allure.title("用户名为空")
    def test_01(self):
        ww =login_action(driver()).log_on(username='', password='123456')
        print(ww,'4324')
        assert "请输入登录ID"== ww
    @pytest.mark.xfail
    @allure.title("用户名为空")
    def test_02(self):
        ww =login_action(driver()).log_on(username='moni1ca', password='123456')
        print(ww,'111')
        assert "账号或密码有误，请检查后重新输入"== ww


if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])
    # TTT = Test_login()
    # TTT.test_01()
