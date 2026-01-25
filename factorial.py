"""
# while loop
a=int(input("Enter the number:"))
fact = 1
i=1
while i<=a:
    fact=fact*i
    i=i+1
    print(fact)"""

# for loop
a=int(input("Enter the number:"))
fact = 1
for i in range(1,a+1):
    fact=fact*i
    print(fact)  #if we print outside the loop the output= only 120