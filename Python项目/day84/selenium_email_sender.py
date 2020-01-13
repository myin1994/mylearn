import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conf import USERNAME, PASSWORD

class SeleniumEmailSender:
    def __init__(self,uname,pwd,browser=None,chrome_options_set=False):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        if not chrome_options_set:
            chrome_options = None
        self.browser = browser or webdriver.Chrome()
        self.uname = uname
        self.pwd =pwd
        self.browser.implicitly_wait(30)
        self.wait = WebDriverWait(self.browser, 10)
        self.login()


    def login(self):
        self.browser.get('https://mail.163.com')
        self.browser.find_element_by_id('switchAccountLogin').click()
        iframe = self.browser.find_elements_by_tag_name('iframe')
        self.browser.switch_to.frame(iframe[0])
        username = self.browser.find_element_by_css_selector('.u-input [name="email"]')
        username.send_keys(self.uname, Keys.TAB, self.pwd, Keys.ENTER)

    def send_email(self,target_name:list,title,centent):
        # time.sleep(5)
        self.browser.find_element_by_id('_mail_component_24_24').click()
        # 写入收件人、主题、正文
        # time.sleep(5)
        # sender = self.browser.find_element_by_class_name('nui-editableAddr-ipt')
        sender = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'nui-editableAddr-ipt')))
        time.sleep(1)
        print(sender)
        sender.send_keys('244797519@qq.com;')
        sender.send_keys(';'.join(target_name)+';', Keys.TAB, title, Keys.TAB, centent)
        # 发送
        self.browser.find_element_by_css_selector('#_mail_button_8_197 > span.nui-btn-text').click()
        # time.sleep(5)
        #回归首页
        self.browser.find_element_by_id('_mail_tabitem_0_3text').click()

    def quit(self):
        time.sleep(100)
        self.browser.quit()
if __name__ == '__main__':
    email_sender = SeleniumEmailSender(USERNAME, PASSWORD,chrome_options_set=True)
    try:
        email_sender.send_email(['244797519@qq.com','3410086155@qq.com'],'无题','内容')
        email_sender.send_email(['244797519@qq.com','3410086155@qq.com'],'无题','内容')
    finally:
        email_sender.quit()