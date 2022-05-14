# 함수 기본 1
def add(a,b):
    return a+b
a=3
b=4
c=add(a,b)
print(c)

# 함수 기본 2
def say():
    return 'Hi'

a = say()
print(a)

# 함수 기본 3
def sum(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))

sum(2,3)

# 함수 기본 4
def say():
    print('Hello')
    
say()

# 함수 기본 5
result = add(a=3, b=4)
print(result)

result2 = add(b=2, a=4)
print(result2)

# 여러 개의 입력 값을 받는 함수 1: *args 
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)
print(result)

result2 = add_many(1,2,3,4,5,6,7,8,9,10)
print(result2)

# 여러 개의 입력 값을 받는 함수 2: *args
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i 
    return result 

result3 = add_mul('add', 1,2,3,4,5)
print(result3)

result4 = add_mul('mul', 1,2,3,4,5)
print(result4)

# 키워드 파라미터 kwargs : **kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.
def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(a=1)
print_kwargs(name='foo', age=3)

#
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result) #출력값 (7,12): 결과값으로 (7,12)라는 튜플 값을 가짐

# 위에서 출력되는 하나의 튜플 값 (7,12)를 2개의 결과값처럼 받고 싶으면 아래와 같이 호출  
result1, result2 = add_and_mul(3,4)

print(result1) #출력값 7
print(result2) #출력값 12

# 매개변수에 초깃값 미리 설정 : 초기화시키고 싶은 매개변수를 항상 뒤쪽에 놓는다.
def say_myself(name, old, man=True): # man=True : 매개변수에 미리 값을 넣어서 매개변수 초기값 설정 
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
        
say_myself('야옹이', 30)
say_myself('나비', 30, False)

# lambda : 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 함. 보통 함수를 한줄로 간결하게 만들 때 사용. 
# lambda 예약어로 만든 함수는 return 명령어가 없어도 결과값을 돌려준다.
add = lambda a,b: a+b
result = add(3,4)
print(result)

