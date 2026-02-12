arr = [10, 30, 10, 20, 50, 30, 60]

visited = []
non_repeating = []

for i in range(len(arr)):
    if arr[i] not in visited:
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        
        if count == 1:          # Store only non-repeating elements
            non_repeating.append(arr[i])
        
        visited.append(arr[i])

print(non_repeating)
