import allure
from selenium.webdriver.common.by import By

from 第9章_App自动化测试_项目实战_test.base.base_action import BaseAction


class HomePage(BaseAction):
    # 更新
    update_button = By.ID, "com.yunmall.lc:id/img_close"

    # 我
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    # 分类
    category_button = By.ID, "com.yunmall.lc:id/tab_category"

    # 点击关闭更新框
    @allure.step(title='点击关闭更新框')
    def click_close_update(self):
        self.click(self.update_button)

    # 点击 我
    @allure.step(title='主页 点击 我')
    def click_me(self):
        self.click(self.me_button)

    # 主页 登录（如果没有登录的话）
    @allure.step(title='主页 登录（如果没有登录的话）')
    def login_if_not(self, page):
        # 判断登录状态
        self.click_me()
        print(self.driver.current_activity)
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return

        # 没有登录，就去登录
        # 点击 已有账号
        page.register.click_login()
        # 输入 用户名
        page.login.input_username("xnh_test")
        # 输入 密码
        page.login.input_password("xnhtest")
        # 点击 登录
        page.login.click_login()

    # 主页 点击 分类
    @allure.step(title='主页 点击 分类')
    def click_category(self):
        self.click(self.category_button)
