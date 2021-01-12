import allure
from selenium.webdriver.common.by import By

from 第9章_App自动化测试_项目实战_test.base.base_action import BaseAction


class VipPage(BaseAction):
    # 邀请码输入框
    invite_edit_text = By.XPATH, "//input[@type='tel']"

    # 点击立即成为会员
    be_vip_button = By.XPATH, "//input[@value='立即成为会员']"

    # vip页面 输入 邀请码
    @allure.step(title='vip页面 输入 邀请码')
    def input_invite(self, text):
        self.input(self.invite_edit_text, text)

    # VIP页面 点击成为会员
    @allure.step(title='VIP页面 点击 成为会员')
    def click_be_vip(self):
        self.click(self.be_vip_button)