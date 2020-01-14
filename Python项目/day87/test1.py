from appium import webdriver


desired_caps = {
    "platformName": "android",
    "platformVersion": "4.4.2",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.jingdong.app.mall",
    "appActivity": "com.jingdong.app.mall.main.MainActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
driver.find_element_by_id('com.jingdong.app.mall:id/beh').click()
driver.find_element_by_id('com.jingdong.app.mall:id/bve').click()