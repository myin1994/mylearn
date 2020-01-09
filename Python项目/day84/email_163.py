import time
from selenium import webdriver  # 驱动浏览器
from selenium.webdriver.common.keys import Keys  # 键盘相关
from selenium.webdriver.support.wait import WebDriverWait  # 等待事件，可以与EC连用
from conf import USERNAME, PASSWORD

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
try:
    browser.get('https://mail.163.com')
    browser.maximize_window()
    # 登录
    login_obj = browser.find_element_by_id('switchAccountLogin').click()
    #切换到iframe框
    iframe = browser.find_elements_by_tag_name('iframe')
    browser.switch_to.frame(iframe[0])
    username = browser.find_element_by_css_selector('.u-input [name="email"]')
    password = browser.find_element_by_css_selector('.u-input [name="password"]')
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD, Keys.ENTER)
    # 发邮件
    # 打开写信
    time.sleep(3)
    browser.find_element_by_id('_mail_component_24_24').click()
    # 写入收件人、主题、正文
    sender = browser.find_element_by_class_name('nui-editableAddr-ipt')
    sender.send_keys('244797519@qq.com', Keys.TAB, '自动发邮件主题', Keys.TAB, '自动发邮件内容')
    #点击发送
    browser.find_element_by_css_selector('#_mail_button_8_197 > span.nui-btn-text').click()
finally:
    time.sleep(10)
    browser.quit()
