a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
root1=(-b-(((b*b)-4*a*c)**(1/2)))/(2*a)
root2=(-b+(((b*b)-4*a*c)**(1/2)))/(2*a)
if root1==root2:
print(root1)
else:
print(root1,root2)
