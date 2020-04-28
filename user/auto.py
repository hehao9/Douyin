import time
from appium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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
    "app": "D:\\PycharmProjects\\Douyin\\DouYin_v6.0.0.apk",
    # 再次启动不需要再次安装
    "noReset": True,
    # unicode键盘 我们可以输入中文
    "unicodeKeyboard": True,
    # 操作之后还原回原先的输入法
    "resetKeyboard": True
}
driver = webdriver.Remote(server, desired_caps)
wait = WebDriverWait(driver, 15)
# 弹出框点击取消按钮
try:
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/sy')
except NoSuchElementException:
    pass
else:
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/sy').click()
# 点击首页搜索图标
wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/aqz'))).click()
# 搜索输入框输入关键字
wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/agq'))).clear().send_keys('成都')
# 然后点击搜索按钮
wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/agt'))).click()
# 点击视频选项卡
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='用户']"))).click()
# 循环
for p in range(1):
    # 点击进入第1个用户
    time.sleep(1)
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@resource-id='com.ss.android.ugc.aweme:id/o7']/android.widget.RelativeLayout[1]"))).click()
    # 点击喜欢选项卡
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@resource-id='com.ss.android.ugc.aweme:id/ak6']/android.widget.HorizontalScrollView"
                   "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]"))).click()
    # 返回
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/nj').click()
    # 向上滑动一条用户信息
    destination_el = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@resource-id='com.ss.android.ugc.aweme:id/o7']/android.widget.RelativeLayout[1]")))
    origin_el = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@resource-id='com.ss.android.ugc.aweme:id/o7']/android.widget.RelativeLayout[2]")))
    driver.scroll(origin_el, destination_el)
# 退出
driver.quit()