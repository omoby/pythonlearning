from selenium.webdriver import Chrome
import time

browser = Chrome('D:\pycharmproject\pythonlearning\webdriver\chromedriver.exe')
browser.get('http://www.porters.vip/features/webdriver.html')

script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'


browser.execute_script(script)

time.sleep(1)
browser.find_element_by_css_selector('.btn.btn-primary.btn-lg').click()

elements = browser.find_element_by_css_selector('#content')

time.sleep(1)
print(elements.text)
browser.close()