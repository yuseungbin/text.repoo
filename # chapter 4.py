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

#q6
user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')   # 내용을 추가하기 위해서 'a'를 사용
f.write(user_input)
f.write("\n")               # 입력된 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입
f.close()

#q7
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()
