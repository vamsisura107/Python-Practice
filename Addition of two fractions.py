n1=int(input("enter the first fraction nemaratorn:"))
dn1=int(input("enter the first fraction denomenator:"))
n2=int(input("enter the second fraction denomenator"))
dn2=int(input("enter the second fraction denomenator"))
numerator=n1*dn2+n2*dn1
denomenator=dn1*dn2
a=numerator
b=denomenator
hcf=1
for i in range(1,min(a,b)+1):
   if a%i==0 and b%i==0:
       hcf=i
numerator//=hcf
denomenator//=hcf
print(numerator,"/",denomenator)
