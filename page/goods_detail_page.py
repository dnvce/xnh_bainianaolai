import time

import allure
from selenium.webdriver.common.by import By
from 第9章_App自动化测试_项目实战_test.base.base_action import BaseAction


class GoodsDetailPage(BaseAction):

    # 加入购物车 按钮
    add_shop_cart_button = By.ID, "com.yunmall.lc:id/btn_add_to_shopping_cart"
    # 确认 按钮
    commit_button = By.XPATH, "//*[@text='确认']"

    # 商品详情 点击 添加购物车
    @allure.step(title='商品详情 点击 添加购物车')
    def click_add_shop_cart(self):
        self.click(self.add_shop_cart_button)

    # 商品详情 点击 确认
    @allure.step(title='商品详情 点击 确认')
    def click_commit(self):
        self.click(self.commit_button)

    # 根据 "请选择 分类 规格" 获取 请选择后面的第一个规格的名字   --- 商品详情 获取第一个规格的词语
    @allure.step(title='商品详情 获取第一个规格的词语')
    def get_choose_spec(self, text):
        return text.split(" ")[1]

    # 商品详情 选择规格
    @allure.step(title='获取商品的标题')
    def click_spec(self):
        while True:
            # 默认不选择规格，直接点击
            self.click_commit()
            # 判断 请选择toast是否存在，如果存在获取规格
            if self.is_toast_exist("请选择"):
                # 获取 颜色分类规格
                spec_name = self.get_choose_spec(self.get_toast_text("请选择"))
                print(spec_name)
                # 获取切割之后的名称
                spec_feature = By.XPATH, "//*[@text='%s']/../*[2]/*[1]" % spec_name
                print(spec_feature)
                # 进行点击
                self.click(spec_feature)
                time.sleep(2)
            else:
                break