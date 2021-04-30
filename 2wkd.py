#q1
국어 = 80
영어 = 75
수학 = 55
print((국어 + 영어 + 수학)/3)

#q2
x=13
if x%2 == 0:
    print("Even")
else:
    print("odd")

#q3
x= "881120-1068234"
print(x[:6])
print(x[7:])
print(x[7])

#q4
a = "a:b:c:d"
print(a.replace(":","$"))

#q5
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#q6
a = ["life", "is", "too", "short"]
print(" ".join(a))

#q8
a = (1,2,3)
b = a+(4,)
print(b)
#q10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)            
print(result)  

#q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(set(a))   

#q12
a = b = [1, 2, 3]
a[1] = 4
print(b)