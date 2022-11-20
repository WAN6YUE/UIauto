# from selenium import webdriver
# from selenium.webdriver.common.by import By#定位元素
# from selenium.webdriver.common.action_chains import ActionChains #鼠标操作
#
# import time
#
#
# url = "http://www.baidu.com"
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)#全局等待=隐式等待  等待只针对定位操作
#
# # driver.set_window_size(400,400) # 设置浏览器宽 高
# # driver.maximize_window()        #撑满屏幕
#
# driver.get(url)
#
# driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('csdn官网\n')
#
# csdn_conent=driver.find_element(By.XPATH,'//*[@id="1"]/div/div[1]/div[2]/div/div[2]/span')
#
# print(driver.current_window_handle)#当前句柄
# print(driver.window_handles)#所有句柄
#
# csdn =driver.find_element(By.XPATH,'//*[@id="1"]/div/div[1]/h3/a[1]').click()
#
# print(driver.current_window_handle)#当前句柄
# print(driver.window_handles)#所有句柄
#
# driver.switch_to.window(driver.window_handles[-1])
#
# print(driver.current_window_handle)#当前句柄
# print(driver.window_handles)#所有句柄
#
# driver.switch_to.window(driver.window_handles[0])
#
# time.sleep(2)
#
# print(csdn_conent.text)
# print(csdn_conent.get_attribute('class'))
# print(csdn_conent.get_attribute('outerHTML'))
# print(csdn_conent.get_attribute('innerHTML'))
#
# #获得页面信息
# print(driver.title)#获得当前页面标题
# print(driver.current_url)#获得当前页面URL
# driver.quit()
#
# # try:
# #     assert(driver.title=='csdn官网_百度搜索'),""
# #     print('成功')
# # except:
# #     print('失败')
# #     driver.quit()
#
#
#
# # print(driver.get_cookies())
#
# # driver.get_screenshot_as_file("D:\\UIautoScreenshot\\test.jpg")#截图并且保存
#
