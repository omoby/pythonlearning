# from selenium import webdriver
#
# driver = webdriver.Chrome('C:\Program Files\driver\chromedriver.exe')
# driver.get("http://m.baidu.com")
#
# # 参数数字为像素点
# print("设置浏览器宽480、高800显示")
# driver.set_window_size(480, 800)
# driver.quit()
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.porters.vip/captcha/sliders.html')
hover = browser.find_element_by_css_selector('.hover')
action = webdriver.ActionChains(browser)
action.click_and_hold(hover).perform()
action.move_by_offset(340, 0)
action.release().perform()