import time
import warnings
warnings.simplefilter('ignore', DeprecationWarning)

from 第9章_App自动化测试_项目实战_test.base.base_driver import init_driver


class TestLogin:
    def setup(self):
        self.driver = init_driver()

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        print("hello")