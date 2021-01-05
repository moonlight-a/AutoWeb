import os
import unittest


import ddt

from Page.login_page import login_action
from public.base import driver
PATH = os.path.dirname(__file__)
test_data_path = PATH + '//YAML//' + 'test_data.yaml'

@ddt.ddt
class run_main(unittest.TestCase):
    def setUp(self) -> None:
        self.login_action = login_action(driver())
    @ddt.file_data(test_data_path)

    def test_login_001(self,**kwargs):

        self.login_action.log_on(**kwargs)


if __name__ == '__main__':
    unittest.main()