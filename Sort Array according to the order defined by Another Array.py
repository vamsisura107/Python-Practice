arr1 = [40, 10, 20, 30, 50, 20]
arr2 = [20, 10, 30]

result = []

# First, add elements according to the order of arr2
for elem in arr2:
    for i in range(arr1.count(elem)):
        result.append(elem)

# Then, add remaining elements that are not in arr2
for elem in arr1:
    if elem not in arr2:
        if elem not in result:  # Prevent duplicates
            result.append(elem)

# Add duplicates of remaining elements
for elem in arr1:
    if elem not in arr2:
        result.append(elem)

print(result)
