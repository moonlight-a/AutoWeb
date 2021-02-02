import pytest

from Page.search_moudle import search_page
from public.base import driver

class Test_organization():

    def test_01(self):
        search_page(driver()).screen_page()

if __name__ == '__main__':
    pytest.main(['-s', 'test_organization.py'])
