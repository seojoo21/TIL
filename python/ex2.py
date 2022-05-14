#1
kor = 80
eng = 75
math = 55

average = (kor+eng+math)/3
print(average)

#4
regNo = "881120-1068234"
print(regNo[:6])
print(regNo[7:])

#5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

#6
c = [1,3,5,4,2]
c.sort()
c.reverse()
print(c)

#7
d = ['Life', 'is', 'too', 'short']
e = " ".join(d)
print(e) 

#8
t1 = (1,2,3)
t2 = (4,)
t3 = t1 + t2
print(t3)

#9
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
a[250] = 'python'
print(a)

#10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(result)
print(a)
print(a.get('C'))
print(a['A'])


#11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
aSetList = list(aSet)
print(aSetList)

#12
a = b = [1,2,3]
a[1]=4
print(b)
