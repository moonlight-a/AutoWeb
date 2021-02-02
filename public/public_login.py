import pytest
from Page.login_page import login_action
from public.base import driver


@pytest.fixture()
def login_fixture():
    login_action(driver()).log_on(username= 'monica',password = '123456')