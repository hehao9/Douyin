import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

server = 'http://localhost:4723/wd/hub'
desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    # 自动化测试包名
    "appPackage": "com.ss.android.ugc.aweme",
    # 自动化测试Activity
    "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
    "automationName": "UiAutomator1",
    # 再次启动不需要再次安装
    "noReset": True,
    # unicode键盘 我们可以输入中文
    "unicodekeyboard": True,
    # 操作之后还原回原先的输入法
    "resetkeyboard": True
}
driver = webdriver.Remote(server, desired_caps)
wait = WebDriverWait(driver, 10)
search = wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/aqz')))
search.click()
saerch_input = wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/agq')))
saerch_input.send_keys('成都')

