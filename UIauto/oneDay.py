# from selenium import webdriver
# from webdriver_helper import get_webdriver
# from selenium.webdriver.common.by import By
# import time
#
#
# baidu_URL='http://www.baidu.com'
# JD_URL='https://www.jd.com/'
# kw='苹果手机'
# # driver = webdriver.Chrome()
# driver = get_webdriver()#导入webdriver_helper 自动获得webdriver 好处：浏览器升级后可以不用升级相应的driver
# driver.implicitly_wait(10)
# driver.get(JD_URL)
# # driver.get_screenshot_as_file("访问百度截图.png")
# # driver.maximize_window()
# # driver.get_screenshot_as_file("最大化_访问百度截图.png")
#
# # title = driver.title
# # html = driver.page_source
# # print(title)
# # print(html)
#
# # baidu_input= driver.find_element(By.XPATH,'//*[@id="kw"]')
# # baidu_input.clear()
# # baidu_input.send_keys("WAN6YUE CSDN")
# # time.sleep(3)
# # baidu_click =driver.find_element(By.XPATH,'//*[@id="su"]')
# # baidu_click.click()
# # time.sleep(3)
# #
# # csdn_link =driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/div[3]/div/div/div[1]/h3/a')#链接列表
# # print(csdn_link)
#
# jingdong_input =driver.find_element(By.XPATH,'//*[@id="key"]')
# jingdong_input.send_keys(kw)
#
# jingdong_click =driver.find_element(By.XPATH,'//*[@id="search"]/div/div[2]/button')
# jingdong_click.click()
#
# shouji_list = driver.find_elements(By.XPATH,'/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li/div/div[4]/a/em')#注意定位一组元素 用find_elements
#
#
#
# print('列表长度为：',len(shouji_list))
# assert len(shouji_list) == 30 or len(shouji_list) > 25
#
#
#
# for i in shouji_list:
#     print(i.text)
#     print()
#
# for i in shouji_list:
#     assert 'apple' or '苹果' in i.text
#
#
#
#
# driver.quit()#关闭浏览器
# #driver.close()关闭当前tab页
#
#
# #脚本缺点
# # 1.代码相似 无法重用 增加了工作量
# # 2.元素加载延迟
# # 3.浏览器重复启动 关闭
#
# #解决方式：通过封装框架的方式 自动解决常见的问题