# 예외 처리
try:
    4/0
except ZeroDivisionError as e:
    print(e)
    
print("hello")

# 예외 처리
try:
    f = open("none.txt", 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()
    
print("hello")

# 예외 처리
f = open('foo.txt', 'w')
try:
    data = f.read()
    print(data)
except Exception as e:
    print(e)
finally:
    f.close()
    
print("hello")