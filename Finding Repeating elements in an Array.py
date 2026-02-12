arr = [10, 30, 10, 20, 10, 30, 20, 10]

visited = []

for i in range(len(arr)):
    if arr[i] not in visited:
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        
        if count > 1:   # Print only repeating numbers
            print(arr[i])
        
        visited.append(arr[i])
