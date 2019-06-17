from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page

import pytest


class TestContact:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # @pytest.mark.parametrize(("name", "phone"), [("zhangsan", "188"), ("lisi", "177")])
    @pytest.mark.parametrize("args", analyze_data("contact_data", "test_add_contact"))
    def test_add_contact(self, args):
        name = args["name"]
        phone = args["phone"]

        # 联系人列表 - 点击 新建联系人
        self.page.contact_list.click_new_contact()
        # 新建联系人 - 输入 姓名
        self.page.new_contact.input_name(name)
        # 新建联系人 - 输入 电话
        self.page.new_contact.input_phone(phone)

    # @pytest.mark.parametrize(("name", "phone"), [("zhangsan", "188"), ("lisi", "177")])
    # def test_delete_contact(self, name, phone):
    #     # 联系人列表 - 点击 新建联系人
    #     self.page.contact_list.click_new_contact()
    #     # 新建联系人 - 输入 姓名
    #     self.page.new_contact.input_name(name)
    #     # 新建联系人 - 输入 电话
    #     self.page.new_contact.input_phone(phone)