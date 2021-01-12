import time

import allure
from selenium.webdriver.common.by import By

from 第9章_App自动化测试_项目实战_test.base.base_action import BaseAction


class MePage(BaseAction):
    # 昵称
    nick_name_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    # 加入VIP
    be_vip_button = By.XPATH, "//*[@text='加入超级VIP']"

    # 设置按钮
    setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    # 我 获取 昵称
    @allure.step(title='我 获取 昵称')
    def get_nick_name_text(self):
        return self.find_element(self.nick_name_text_view).text

    # 我 点击 加入vip
    @allure.step(title='我 点击 加入vip')
    def click_be_vip(self):
        self.find_element(self.be_vip_button).click()
        # 暂定2秒，由于webview页面加载比较慢
        time.sleep(2)

    # 我 点击 设置
    @allure.step(title='我 点击 设置')
    def click_setting(self):
        self.find_element_with_scroll(self.setting_button).click()