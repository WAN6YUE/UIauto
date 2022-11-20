# 使用pytest
# 1.创建test_开头的python文件
# 2.创建test_开头的函数（或者Test开头的类）
# 3.创建测试用例
# 4.执行测试用例
# 5.标准启动方式   终端命令->pytest
import allure
import pytest

#  . 通过
#  F 失败
#  E 出错 ->框架问题
#  s 跳过


# #一个函数代表一个测试用例
# def test_case_one():#测试用例
#     assert 1 == 1
#
# class TestClassOne:#这个类包含两个函数 即两个测试用例  类是测试套件不属于测试用例
#     def test_case_two(self,driver):#测试用例
#         assert 2 == 1
#     def test_case_three(self,driver):#测试用例
#         assert 1 == 2


# pytest的fixture  fixture(夹具)可以在测试用例的执行之前和执行之后 自动地去执行一些代码
# 也可以把不用用例中 相同的代码经行复用 ，在不同用例中 实现依赖的管理

# 1.创建夹具 夹具本质是一个函数  函数加上fixture装饰器可成为夹具  即：夹具=函数+fixture装饰器
# 2.使用夹具 ：在测试用例的参数列表中 加上夹具名称 夹具就会被自动使用

# fixture范围 创建夹具时 可以指定夹具共享范围 在共享范围内的用例 在共享范围内的case会 会共用同一个夹具

# pytest的夹具 共享范围有5种
# 1.默认 function  最小范围-不共享
# 2. class
# 3.module  模块 /文件
# 4.package 包 /文件夹
# 5.session 会话  从启动pytest到结束 最大范围-全局共享


# POM (page object module) 实现对页面的封装   页面对象模型
# POM通过面向对象的思想 封装页面中的元素，以及在页面中经行自动化操作


# 参数化测试 +数据文件 =数据驱动测试

from core.pages import *
from core.ddt import read_csv


class TestJd:  # 类需要Test开头
    @pytest.mark.parametrize("data",read_csv(r'datas/search.csv'))
    def test_zhengxiang(self, driver,data):  # 正向用例 函数需要test_开头
        # driver.get('https://www.jd.com/')#打开被测网页
        # page =IndexPage(driver)#利用IndexPage 实例化po
        page = IndexPage.start(driver)  # 代表自动跳转到被测页面 并实例化po 代表上面两行
        page = page.search(data['wd'])  # 调用IndexPage方法search 传入苹果手机  --自动化操作 返回值可以实例化下一个po

        # page=SearchPage(driver)#因为跳转了页面 需要实例化新的po
        text_list = page.get_all_text()  # 使用SearchPage返回文本-执行自动化操作
        allure.attach(driver.get_screenshot_as_png(),"页面截图")
        print(len(text_list))
        assert str(len(text_list)) == data['count']  # 断言结束数据的len

        for i in text_list:
            assert data['assert'] in i  # 断言结果数据的文本

    # def test_fanxiang(self, driver):  # 反向用例 函数需要test_开头
    #     # driver.get('https://www.jd.com/')  # 打开被测网页
    #     # page = IndexPage(driver)  # 利用IndexPage 实例化po
    #
    #     page = IndexPage.start(driver)  # 代表自动跳转到被测页面 并实例化po 代表上面两行
    #     page = page.search('巴拉巴拉')  # 调用IndexPage方法search 传入苹果手机  --自动化操作
    #
    #     # page = SearchPage(driver)  # 因为跳转了页面 需要实例化新的po
    #     text_list = page.get_all_text()  # 使用SearchPage返回文本-执行自动化操作
    #     print(len(text_list))
    #     assert len(text_list) != 0  # 断言结束数据的len
    #
    #     for i in text_list:
    #         assert 'apple' not in i or 'Apple' not in i or '苹果' not in i  # 断言结果数据的文本

# 问题 用例执行失败的时候 未关闭浏览器
