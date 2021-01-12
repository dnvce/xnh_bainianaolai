import time

from 第9章_App自动化测试_项目实战_test.base.base_driver import init_driver
from 第9章_App自动化测试_项目实战_test.page.page import Page


class TestShopCart:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_add_shop_cart(self):
        # 0.关闭更新
        self.page.home.click_close_update()
        # 1.首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 2.首页 - 分类
        self.page.home.click_category()
        # 3.分类 - 商品列表
        self.page.category.click_goods_list()
        # 4.商品列表 - 商品详情
        self.page.goods_list.click_goods()
        # 5.商品详情 - 加入购物车
        self.page.goods_detail.click_add_shop_cart()
        # 6.商品详情 - 选择规格
        self.page.goods_detail.click_spec()

        time.sleep(2)