num = int(input("enter the number"))
temp = num
sum = 0
length = len(str(num))

for _ in range(length):
    digit = temp % 10
    temp = temp // 10
    sum = sum + (digit ** length)

if sum == num:
    print("armstrong number")
else:
    print("not an armstrong number")
