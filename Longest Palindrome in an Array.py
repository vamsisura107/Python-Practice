arr=list(map(int,input().split(‘,’)))
p=[]
for num in arr:
 if str(num)[::-1]== str(num):
   p.append(str(num))
if p:
   longest_palindrome= max(p)
   print(longest_palindrome)
else:
   print("No Palindrome found.")
