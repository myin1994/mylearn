import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from conf import USERNAME, PASSWORD


def email_sender(browser,uname,pwd,target_name,title,centent):
    wait = WebDriverWait(browser, 20)
    try:
        browser.get('https://mail.163.com')
        browser.find_element_by_id('switchAccountLogin').click()
        iframe = browser.find_elements_by_tag_name('iframe')
        browser.switch_to.frame(iframe[0])
        username = browser.find_element_by_css_selector('.u-input [name="email"]')
        username.send_keys(uname,Keys.TAB,pwd, Keys.ENTER)
        time.sleep(3)
        browser.find_element_by_id('_mail_component_24_24').click()
        # 写入收件人、主题、正文
        sender = browser.find_element_by_class_name('nui-editableAddr-ipt')
        sender.send_keys(target_name, Keys.TAB, title, Keys.TAB, centent)
        #发送
        browser.find_element_by_css_selector('#_mail_button_8_197 > span.nui-btn-text').click()
        time.sleep(20000)
    except Exception as e:
        print(e)
    finally:
        time.sleep(1000000)
        browser.quit()
if __name__ == '__main__':
    browser = webdriver.Chrome()
    email_sender(
        browser,
        USERNAME,
        PASSWORD,
        '244797519@qq.com',
        '自动发邮件主题',
        '自动发邮件内容'
    )