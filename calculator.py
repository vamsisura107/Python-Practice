a = int(input("enter the  value: "))
b = int(input("enter the  value: "))
calc=input("enter your choice: ")
if calc=="+":
    print(f"addition is {a+b} ")
elif calc=="-":
    print(f"substraction is {a-b} ")
elif calc=="*":
    print(f"multiplication {a*b}")
elif calc=="/":
    print(f"division  {a/b}")
else:
    print("not define")