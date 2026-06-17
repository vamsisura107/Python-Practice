n = int(input("Enter the number: "))
prime_factors = []
flag=0
for i in range(2, n + 1):
    if n % i == 0:
        flag=1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                flag=0
                break
        if flag==1:
            prime_factors.append(i)
print("Prime factors are:", prime_factors)
