import requests 
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") #lxml parser를 통해 BeautifulSoup 객체로 만든다.
print(soup.title) #<title></title> 태그를 가져온다. 
print(soup.title.get_text()) #<title></title> 태그 내 텍스트만 가져온다. 
print(soup.a) #soup 객체로 담긴 html 정보 내에서 첫번째 a 태그를 출력한다. 
print(soup.a.attrs) #soup 객체로 담긴 html 정보 내 첫번째 a 태그의 속성 정보들을 출력한다. 
print(soup.a["href"]) #["원하는 속성값"] : 원하는 속성값 정보를 출력한다.

print(soup.find("a", attrs={"class":"Nbtn_upload"}))
#soup 객체 내 모든 내용 중에서 a element의 class 속성이 "Nbtn_upload"인 element를 찾아서 출력한다. 
print(soup.find(attrs={"class":"Nbtn_upload"}))
#soup 객체 내 모든 내용 중에서 class 속성이 "Nbtn_upload"인 어떤 element를 찾아서 출력한다. 

###############################################################################
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)
#rank1에 담긴 element에서 a element를 찾아서 출력한다.

#### 1. 형제 가져오기 ####
print(rank1.next_sibling) 
#rank1의 다음 형제 element를 가져온다. 개행문자가 있을 경우 공백으로 나타난다.
#개행문자가 있어 공백으로 나타날 경우 print(rank1.next_sibling.next_sibling)과 같이 next_sibling을 추가해주면 된다.

rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

#### 2. 부모 가져오기 ####
print(rank1.parent)

#### 3. next_sibling/previous_sibling 여러 번 쓰지 않고 바로 원하는 값 가져오기 ####
print(rank1.find_next_sibling("li")) 
#위의 코드는 print(rank1.next_sibling.next_sibling) 과 같다.
print(rank2.find_previous_sibling("li"))

#### 4. 형제들 가져오기 ####
print(rank1.find_next_siblings("li"))

###############################################################################
