lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print(f"Prime numbers between {lower} and {upper} are:")
for num in range(lower, upper + 1):
    if num <= 1:
        continue
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
    if flag == 0:
        print(num, end=" ")
print()
