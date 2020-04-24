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
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='视频']"))).click()
# 点击进入第一个视频
wait.until(EC.presence_of_element_located(
    (By.XPATH, "//*[@resource-id='com.ss.android.ugc.aweme:id/o7']/android.widget.FrameLayout[1]"))).click()
# 循环
for n in range(2):
    # 点击查看评论
    time.sleep(1)
    driver.tap([(668, 876)], 500)
    # 点击上方空白区域关闭评论
    wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/azk'))).click()
    # 向上滑动，获取下一个视频
    time.sleep(1)
    size = driver.get_window_size()
    driver.swipe(size['width'] * 0.5, size['height'] * 0.75, size['width'] * 0.5, size['height'] * 0.25, 500)
# 推出
driver.quit()
