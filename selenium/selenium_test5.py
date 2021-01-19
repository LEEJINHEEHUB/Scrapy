from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:\\work\\chromedriver.exe"
driver = webdriver.Chrome(path)

# selenium을 통해 (facebook) 로그인 정보 전달 후 자기 프로필, 그룹 보기

driver.get("https://www.facebook.com")
print(driver.title)

elem_email = driver.find_element_by_id("email")
elem_email.send_keys("01095512549")
elem_pass = driver.find_element_by_id("pass")
elem_pass.send_keys("dl18759053!?@")

elem_pass.send_keys(Keys.RETURN)
#개발자 도구로 해당 부분 <div>태그 위에 <a>태그 를 copy Xpath 해야함 (중요)
profile_a = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a')
print("Porfile A =>", profile_a.get_attribute('href'))

friends_a = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/a')
print("Friends A =>", friends_a.get_attribute('href'))

#해당 페이지 이동
# driver.get(profile_a.get_attribute('href'))
driver.get(friends_a.get_attribute('href'))





