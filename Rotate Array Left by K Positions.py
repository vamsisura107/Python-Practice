arr = [1, 2, 3, 4, 5]
k = 2
k = k % len(arr)
result = []
for i in range(k, len(arr)):
    result.append(arr[i])
for i in range(0, k):
    result.append(arr[i])
print("Rotated Array:", result)
