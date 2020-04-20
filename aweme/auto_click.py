import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
wait = WebDriverWait(driver, 20)
# 点击首页搜索图标
wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/aqz'))).click()
# 搜索输入框输入关键字
wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/agq'))).send_keys("成都")
# # 然后点击搜索按钮
# wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/agt'))).click()
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]').click()
