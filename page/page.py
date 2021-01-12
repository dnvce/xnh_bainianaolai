from 第9章_App自动化测试_项目实战_test.page.address_list_page import AddressListPage
from 第9章_App自动化测试_项目实战_test.page.category_page import CategoryPage
from 第9章_App自动化测试_项目实战_test.page.edit_address_page import EditAddressPage
from 第9章_App自动化测试_项目实战_test.page.goods_detail_page import GoodsDetailPage
from 第9章_App自动化测试_项目实战_test.page.goods_list_page import GoodListPage
from 第9章_App自动化测试_项目实战_test.page.home_page import HomePage
from 第9章_App自动化测试_项目实战_test.page.login_page import LoginPage
from 第9章_App自动化测试_项目实战_test.page.me_page import MePage
from 第9章_App自动化测试_项目实战_test.page.register_page import RegisterPage
from 第9章_App自动化测试_项目实战_test.page.setting_pge import SettingPage
from 第9章_App自动化测试_项目实战_test.page.vip_page import VipPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    # 进入首页
    @property
    def home(self):
        return HomePage(self.driver)

    # 登录页面
    @property
    def login(self):
        return LoginPage(self.driver)

    # 注册页面
    @property
    def register(self):
        return RegisterPage(self.driver)

    # 我 按钮
    @property
    def me(self):
        return MePage(self.driver)

    # 进入VIP页面
    @property
    def vip(self):
        return VipPage(self.driver)

    # 设置
    @property
    def setting(self):
        return SettingPage(self.driver)

    # 地址列表
    @property
    def address_list(self):
        return AddressListPage(self.driver)

    # 编辑地址
    @property
    def edit_address(self):
        return EditAddressPage(self.driver)

    # 分类页面
    @property
    def category(self):
        return CategoryPage(self.driver)

    # 商品详情
    @property
    def goods_detail(self):
        return GoodsDetailPage(self.driver)

    # 商品列表
    @property
    def goods_list(self):
        return GoodListPage(self.driver)


