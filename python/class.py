# 클래스 생성 
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result 
    def mul(self):
        result = self.first * self.second
        return result 
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
        
# a = FourCal()
# a.setData(3,7)
# print(a.first)
# print(a.second)

# print("-----------")
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())
# print("-----------")

# a = FourCal(4,2)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

# 클래스 상속 
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
# 메소드 오버라이딩 
class safeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else: 
            return self.first / self.second

# a = safeFourCal(4,0)
# print(a.div())

# 클래스 변수 
class Family:
    lastname = "김"
    
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "박"
print(a.lastname)
print(b.lastname)

a.lastname = "최"
print(a.lastname)
print(b.lastname)

