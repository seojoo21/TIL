from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# 페이지 이동 
browser.get("http://naver.com")

# 네이버 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login") 
elem.click()

browser.back() # 페이지 뒤로 이동 
browser.forward() # 페이지 앞으로 이동 
browser.refresh() # 페이지 새로고침 

# 네이버 검색창 찾기 
elem = browser.find_element_by_id("query")
# 네이버 검색창에 검색어 입력
elem.send_keys("안녕하세요")
# 검색어 입력 후 엔터키 누름 
elem.send_keys(Keys.ENTER)

# 모든 a 태그 가져오기 
elem = browser.find_elements_by_tag_name("a")
# 모든 a 태그 내에서 href 속성 값만 가져오기 
for e in elem:
    e.get_attribute("href")

# 브라우저 전체 종료 
browser.quit()