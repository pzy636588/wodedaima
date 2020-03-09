from selenium import webdriver
#执行到这里的时候 Selenium会到指定的路径将chrome driver程序运行起来
driver=webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# get方法 打开指定网址
driver.get("http://www.baidu.com")
print(driver.get_cookies())
driver.find_element_by_id("kw").send_keys("阿里巴巴")

driver.find_element_by_id("su").click()