arr = [4, 5, 0, 1, 9, 0, 5, 0]
result = []
for num in arr:
    if num != 0:
        result.append(num)
zeros_needed = len(arr) - len(result)
for i in range(zeros_needed):
    result.append(0)
print("Processed Array:", result)
