import time
import pytest

from 第9章_App自动化测试_项目实战_test.base.base_analyze import analyze_file
from 第9章_App自动化测试_项目实战_test.base.base_driver import init_driver
from 第9章_App自动化测试_项目实战_test.page.page import Page


class TestVip:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("vip_data.yaml","test_vip"))
    def test_vip(self, args):
        keyword = args["keyword"]
        expect = args["expect"]

        # 关闭更新
        self.page.home.click_close_update()
        # 0.如果没有登录则需要先登录
        self.page.home.login_if_not(self.page)
        # 1.首页点击我
        self.page.home.click_me()
        # 2. 我 点击 加入vip
        self.page.me.click_be_vip()
        # 3. 切换web环境
        print(self.driver.contexts)
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        # 4. 输入邀请码
        self.page.vip.input_invite(keyword)
        # 5. 点击加入会员
        self.page.vip.click_be_vip()
        # 7. 断言，"邀请码输入不正确" 是否在 page_source 中
        # assert self.page.vip.is_keyword_in_page_source("邀请码输入不正确"), "邀请码输入不正确，不在page_source中"
        assert self.page.vip.is_keyword_in_page_source(expect), "%s不在page_source中" % expect
        # 6. 切换原生环境
        self.driver.switch_to.context("NATIVE_APP")

