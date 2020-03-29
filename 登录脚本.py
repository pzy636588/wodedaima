from selenium import webdriver
from selenium.webdriver.common.keys import Keys #键盘事件引入keys包
import time
from selenium.webdriver.common.action_chains import ActionChains  #鼠标事件引入ActionChains包

# 注意：17行用户名、19行密码、25行活动名、55行活动链接均未参数化

driver = webdriver.Chrome()  #启动谷歌浏览器
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe" #这里写本地的chromedriver 的所在路径
driver.maximize_window()  #窗口最大化
