#q1
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#q2
sum = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        sum += i
    i += 1
print(sum)

#q3
i = 0
while True:
    i += 1
    if i > 5:
        break
    print ('*' * i) 