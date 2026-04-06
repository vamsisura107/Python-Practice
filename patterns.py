#Right Triangle Star Pattern
n = 5
for i in range(1, n+1):
    print("* " * i)
#inverted Right Triangle Star Pattern
n = 5
for i in range(n, 0, -1):
    print("* " * i)
#pyramid Pattern
n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)
# inverted pyramid Pattern
n = 5
for i in range(n, 0, -1):
    print(" " * (n-i) + "* " * i)
 #Diamond Pattern
n = 5
# Upper part
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)
# Lower part
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "* " * i)
#Number Triangle
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
#Floyd's Triangle
n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
#pascal's Triangle
n = 5
for i in range(n):
    num = 1
    for j in range(n-i):
        print(" ", end="")
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()
#Hallow Square pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#Alphabet Pattern
