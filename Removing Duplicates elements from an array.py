arr = [10, 20, 40, 30, 50, 20, 10, 20]

unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print(unique)
