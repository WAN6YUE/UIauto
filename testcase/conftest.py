#pytest约定的夹具 名称 conftest.py
from webdriver_helper import get_webdriver
import pytest

@pytest.fixture(scope='class')#scope指定范围
def driver():
    d = get_webdriver()#启动浏览器
    yield d #此行前的代码 在测试用例执行之前执行  此后的代码  在测试用例之后执行
    d.quit()#关闭浏览器