arr = [1, 2, 3, 4, 4]
even_count = 0
odd_count = 0

for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count:", even_count)
print("Odd count:", odd_count)
