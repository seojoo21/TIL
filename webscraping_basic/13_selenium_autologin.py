from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# 1. 네이버 이동 
browser.get("http://naver.com")

# 2. 네이버 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login") 
elem.click()

# 3. id, pw 입력 
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# 5. id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력 
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료 
browser.quit() # 전체 브라우저 종료 