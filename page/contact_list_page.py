from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ContactListPage(BaseAction):

    # 新建联系人
    new_contact_button = By.ID, "com.android.contacts:id/floating_action_button"

    # 点击 新建联系人
    def click_new_contact(self):
        self.click(self.new_contact_button)