from appium import webdriver


class Driver:
    app_driver = None

    @classmethod
    def get_app_driver(cls):
        # 判断
        # driver不存在，先声明
        if not cls.app_driver:
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings'
            }
            cls.app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            return cls.app_driver
        else:
            # 已经存在，直接打开
            return cls.app_driver

    @classmethod
    def quit_app_driver(cls):
        # 判断存在则关闭
        if cls.app_driver:
            cls.app_driver.quit()
            cls.app_driver = None
