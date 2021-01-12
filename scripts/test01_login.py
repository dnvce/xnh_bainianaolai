import time
import pytest

from 第9章_App自动化测试_项目实战_test.base.base_analyze import analyze_file
from 第9章_App自动化测试_项目实战_test.page.page import Page
from 第9章_App自动化测试_项目实战_test.base.base_driver import init_driver


class TestLogin:
    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    def test_login(self, args):
        # 解析 yaml 的数据
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        # 0.关闭更新
        self.page.home.click_close_update()
        # 1.首页点击我
        self.page.home.click_me()
        # 2.注册点击登录
        self.page.register.click_login()
        # 3.登录输入用户名
        self.page.login.input_username(username)
        # 4.登录输入密码
        self.page.login.input_password(password)
        # 5.登录点击登录
        self.page.login.click_login()
        # 6.断言，如果"我"页面的用户名和输入的用户名一致，那么脚本通过
        if toast is None:
            #     1.创建page / me_page页面
            #     1.获取，并获取用户名文字
            assert self.page.me.get_nick_name_text() == username, "登录后的用户名和输入的用户名一致"
        else:
            # 找toast提示，找args中的toast提示是否能找到，如果能则通过，如果不能则不通过
            assert self.page.login.is_toast_exist(toast)


