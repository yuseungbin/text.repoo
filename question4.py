#q4
for i in range(1,101):
    print(i)

#q5
list = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in list:
    sum += i

print(sum/(len(list)))


#q6
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result)

def averge(x):
    sum = 0
    for i in x:
        sum += i
    return sum/len(x)
averge(input())