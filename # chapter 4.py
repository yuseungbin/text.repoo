#q1
def is_odd(x):
    if x%2 == 0:
        return False
    else:
        return True

print(is_odd(3))

#q2
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

print(avg_numbers(1,2))

#q3
input1 = input("첫 번째 숫자를 입력하세요:")
input2 = input("두 번째 숫자를 입력하세요:")

total = int(input1) + int(input2)

print("두수의 합은 %s 입니다" % total)

#q4
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

#q5
f1 = open("test.txt", 'w')
f1.write("Life is too short!")
f1.close() # 열린 파일 객체를 닫는다.

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()