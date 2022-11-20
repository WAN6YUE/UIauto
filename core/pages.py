#创建page类
import os
import sys
from webdriver_helper.pom import *


class IndexPage(BasePage):#首页
    url='https://www.jd.com/'#小写url

    jingdong_input = LazyElement(By.XPATH,'//*[@id="key"]')#搜索输入框
    jingdong_click = LazyElement(By.XPATH, '//*[@id="search"]/div/div[2]/button')#搜索按钮

    def search(self,wd):
        self.jingdong_input.send_keys(wd)
        self.jingdong_click.click()

        return SearchPage(self.driver)#IndexPage结束后 自动实例化下一个po

class SearchPage(BasePage):#搜索后页面

    search_list = LazyElementList(By.XPATH,'/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li/div/div[4]/a/em')

    def get_all_text(self):
        L = []
        for i in self.search_list:
            L.append(i.text)
        return L



