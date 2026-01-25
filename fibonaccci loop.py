# Fibonacci sequence using loop
n = int(input("Enter how many terms you want: "))
a = 0
b = 1
print("Fibonacci Sequence:")
for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c
#by using recursion
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input("Enter number of terms: "))
for i in range(n):
    print(fib(i), end="")