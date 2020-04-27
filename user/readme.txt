夜神模拟器（分辨率设置-手机版-720*1280）
抖音版本6.0.0
1、启动抓包：mitmdump -s D:\PycharmProjects\Douyin\user\crawler.py
2、启动appium服务
3、执行模拟点击：python D:\PycharmProjects\Douyin\user\auto.py
4、下载并替换视频地址，音乐，头像等链接：python D:\PycharmProjects\Douyin\user\download.py
注：获取'deviceName'，使用命令：adb devices
   获取到'appPackage'和'appActivity'，adb连接上设备后打开应用，使用命令：adb shell dumpsys activity top|findstr ACTIVITY