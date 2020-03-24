from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://i.xue.taobao.com/detail.htm?courseId=114898")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="J_TabBar"]/ul/li[3]'))
    )
    text = driver.page_source
    print("text", text)
finally:
    driver.quit()
