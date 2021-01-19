from selenium import webdriver

path = "C:\\work\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.google.com")
print(driver.title)

#셀레니엄을 통한 특정 사이트에서 내용 전달, 특정사이트에 name을 통해 검색창에 검색어를 입력하여 enter 까지 해주는 작업
search_box = driver.find_element_by_name("q")
search_box.send_keys("아마존 웹 서비스")
search_box.submit()


