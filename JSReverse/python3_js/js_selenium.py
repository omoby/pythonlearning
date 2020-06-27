from selenium import webdriver

url = 'http://www.porters.vip/verify/sign/'
browser = webdriver.Chrome('D:\pycharmproject\pythonlearning\webdriver\chromedriver.exe')
browser.get(url)
browser.find_element_by_css_selector('#fetch_button').click()
resp = browser.find_element_by_css_selector('#content').text
# resp = browser.page_source

print(resp)
browser.quit()