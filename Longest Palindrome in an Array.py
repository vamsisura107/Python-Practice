arr = list(map(int, input("Enter numbers separated by a comma: ").split(",")))
p = []
for i in arr:
    if str(i)[::-1] == str(i):
        p.append(i)
if p:
    largest = max(p)
    print(largest)
else:
    print("Not found")
