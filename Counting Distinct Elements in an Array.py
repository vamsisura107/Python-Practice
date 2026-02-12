x = [10, 20, 40, 30, 50, 20, 10, 20]
y = []

for i in x:
    if i not in y:
        y.append(i)

print("Unique elements:")
for item in y:
    print(item)

print("Total unique elements:", len(y))
