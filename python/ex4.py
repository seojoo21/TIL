# #1
# def is_odd(num):
#     if(num % 2 == 0):
#         print("%d은/는 짝수입니다." %num)
#     elif(num % 2 == 1):
#         print("%d은/는 홀수입니다." %num)

# is_odd(4)

# #2
# def average(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum / len(args)

# result = average(1,2)
# print(result)

# #3 
# input1 = input("첫번째 숫자를 입력하세요:")
# input2 = input("두번째 숫자를 입력하세요:")

# total = int(input1) + int(input2)
# print("두 수의 합은 %s 입니다" % total)

# #5
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()

# f2 = open("test.txt", 'r')
# print(f2.read())

# #6
# input = input("내용을 입력하세요. >>")
# f2 = open("test.txt", 'a')
# f2.write(input)
# f2.write("\n")
# f2.close()

#7
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()