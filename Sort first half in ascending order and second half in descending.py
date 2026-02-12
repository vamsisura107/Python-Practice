a=int(input("enter the number"))
arr=list(map(int,input("enter the number").split(",")))
mid=a//2
fa=sorted(arr[:mid])
sa=sorted(arr[mid:])
print(fa)
print(sa[::-1])
