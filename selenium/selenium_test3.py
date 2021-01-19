from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:\\work\\chromedriver.exe"
driver = webdriver.Chrome(path)

# selenium에 로그인 정보 전달 (github)

driver.get("https://github.com/login")
print(driver.title)

elem_email = driver.find_element_by_id("login_field")
elem_email.send_keys("LEEJINHEEHUB")
elem_pass = driver.find_element_by_id("password")
elem_pass.send_keys("dl18759053!")

elem_pass.send_keys(Keys.RETURN)

