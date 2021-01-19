from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:\\work\\chromedriver.exe"
driver = webdriver.Chrome(path)

# selenium에 로그인 정보 전달 (facebook)

driver.get("https://www.facebook.com")
print(driver.title)

elem_email = driver.find_element_by_id("email")
elem_email.send_keys("01095512549")
elem_pass = driver.find_element_by_id("pass")
elem_pass.send_keys("dl18759053!?@")

elem_pass.send_keys(Keys.RETURN)

