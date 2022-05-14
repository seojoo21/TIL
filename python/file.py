# 파일 생성하기 
# 파일 객체 = open(파일 이름, 파일 열기 모드)
# 파일 열기 모드: r:읽기모드, w:쓰기모드, a:추가모드(파일의 마지막에 새로운 내용 추가)
# f = open("새파일.txt", 'w')
# for i in range(1,11):
#     data = "%d번째 줄입니다.\n" %i
#     f.write(data)
# f.close()

# 파일 읽기1: readline
# f = open("새파일.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# f = open("새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# 파일 읽기2: readlines
# f = open("새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     line = line.strip() # 줄 끝의 줄 바꿈 문자(\n)를 제거한다. 
#     print(line)
# f.close()

# 파일 읽기3: read
# f = open("새파일.txt", 'r')
# data = f.read()
# print(data)
# f.close

# 파일에 새로운 내용 추가하기 
# f = open("새파일.txt", 'a')
# for i in range(11,20):
#     data = "%d번째 줄입니다.\n" %i
#     f.write(data)
# f.close()

