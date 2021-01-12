import allure
from selenium.webdriver.common.by import By

from 第9章_App自动化测试_项目实战_test.base.base_action import BaseAction


class SettingPage(BaseAction):

    # 地址管理 按钮
    address_list_button = By.XPATH, "//*[@text='地址管理']"

    # 在base_action中添加边滑边找元素工具方法
    # 设置 点击 地址管理
    @allure.step(title='设置 点击 地址管理')
    def click_address_list(self):
        self.find_element_with_scroll(self.address_list_button).click()