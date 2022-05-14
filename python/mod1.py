class FourCal:
    # 클래스 변수: 모든 클래스에 공통 적용 
    # first = 2
    # second = 3 
    
    # __init__: 생성자. 객체변수 : 객체마다 다르게 적용 
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
    
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second