import time
import os
from selenium import webdriver
# 先安装pywin32，才能导入下面两个包
import win32api
import win32con
# 导入处理alert所需要的包
from selenium.common.exceptions import NoAlertPresentException
import traceback

# 环境配置
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application"
os.environ["webdriver.ie.driver"] = chromedriver

driver = webdriver.Chrome()  # 选择Chrome浏览器
driver.get('https://www.baidu.com')  # 打开网站
driver.maximize_window()  # 最大化谷歌浏览器
# 处理alert弹窗
try:
    alert1 = driver.switch_to.alert  # switch_to.alert点击确认alert
except NoAlertPresentException as e:
    print("no alert")
    traceback.print_exc()
else:
    at_text1 = alert1.text
    print("at_text:" + at_text1)

time.sleep(1)

# driver.find_element_by_link_text('登录').click() # 点击“账户登录”

'''username = "18888888888"  # 请替换成你的用户名
password = "123456"  # 请替换成你的密码

driver.find_element_by_id('username').click()  # 点击用户名输入框
driver.find_element_by_id('username').clear()  # 清空输入框
driver.find_element_by_id('username').send_keys(username)  # 自动敲入用户名

driver.find_element_by_id('password').click()  # 点击密码输入框
driver.find_element_by_id('password').clear()  # 清空输入框
driver.find_element_by_id('password').send_keys(password)  # 自动敲入密码

# 采用class定位登陆按钮
# driver.find_element_by_class_name('ant-btn').click() # 点击“登录”按钮
# 采用xpath定位登陆按钮，
driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/form/button').click()

time.sleep(1)

# driver.find_element_by_id('signIn').click() # 点击“签到”

win32api.keybd_event(122, 0, 0, 0)  # F11的键位码是122，按F11浏览器全屏
win32api.keybd_event(122, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键'''

# driver.close()

# 代码调用：
# python.exe JDSignup.py
# 可以将这行命令添加到Windows计划任务，每天运行，从而实现每日自动签到领取京豆