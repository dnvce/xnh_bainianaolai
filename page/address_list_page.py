import allure
from selenium.webdriver.common.by import By

from 第9章_App自动化测试_项目实战_test.base.base_action import BaseAction


class AddressListPage(BaseAction):
    # 新增地址 按钮
    add_address_button = By.ID, "com.yunmall.lc:id/address_add_new_btn"

    # 默认的姓名和电话的信息的特征
    default_receipt_name_text_view = By.ID, "com.yunmall.lc:id/receipt_name"

    # 默认标记 特征
    is_default_feature = By.ID, "com.yunmall.lc:id/address_is_default"

    # 编辑 按钮
    edit_button = By.XPATH, "//*[@text='编辑']"

    # 删除 按钮
    delete_button = By.XPATH, "//*[@text='删除']"

    # 确定 按钮
    commit_button = By.XPATH, "//*[@text='确认']"

    # 地址列表 点击 添加地址
    @allure.step(title='地址列表 点击 添加地址')
    def click_add_address(self):
        self.find_element_with_scroll(self.add_address_button).click()

    # 地址列表 获取 收件人和电话的标题
    @allure.step(title='地址列表 获取 收件人和电话的标题')
    def get_default_receipt_name_text(self):
        return self.get_text(self.default_receipt_name_text_view)

    # 判断 默认标记 是否存在
    @allure.step(title='判断默认标记是否存在')
    def is_default_feature_exist(self):
        return self.is_feature_exist(self.is_default_feature)

    # 地址列表 点击 默认地址
    @allure.step(title='地址列表 点击 默认地址')
    def click_default_address(self):
        self.click(self.is_default_feature)

    # 地址列表 点击 编辑
    @allure.step(title='地址列表 点击 编辑')
    def click_edit(self):
        self.click(self.edit_button)

    # 地址列表 点击 删除
    @allure.step(title='地址列表 点击 删除')
    def click_delete(self):
        self.click(self.delete_button)

    # 判断 删除按钮 是否存在
    @allure.step(title='判断 删除按钮 是否存在')
    def is_delete_exist(self):
        return self.is_feature_exist(self.delete_button)

    # 点击 确定
    def click_commit(self):
        self.click(self.commit_button)