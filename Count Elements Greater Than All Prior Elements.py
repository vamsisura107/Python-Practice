arr = [7, 4, 8, 2, 9]
count = 1
max_so_far = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_so_far:
        count += 1
        max_so_far = arr[i]
print("Elements greater than all prior:", count)
