import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 创建浏览器对象
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)

# 访问URL
driver.get('https://www.baidu.com')
print(driver.title)  # 百度一下，你就知道
time.sleep(1)
driver.quit()