抖音版本6.0.0
1、启动抓包：mitmdump -s D:\PycharmProjects\douyin\aweme\mitmdump.py
2、启动APP模拟点击：python D:\PycharmProjects\douyin\aweme\appium.py
获取'deviceName'，使用命令：adb devices
获取到'appPackage'和'appActivity'，adb连接上设备后打开应用，使用命令：adb shell dumpsys activity top|findstr ACTIVITY