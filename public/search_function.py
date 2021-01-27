import os

import yaml

from public.opertion_element import Element

PATH = os.path.dirname(os.path.dirname(__file__))
element_load = yaml.load(open(PATH + '//page_elements//page_element.yaml', 'r', encoding='utf-8'))
class search_moudle(Element):


    def search_input_text(self):
        input_text = self.find_elements_class(element_load.get('input_text_element'))

        return input_text


    def search_select(self):
        filter_data = []
        select_value = self.find_elements_class(element_load.get('check_select_value_element'))

        [filter_data.append(x) for x in select_value if x.text != '']
        return filter_data