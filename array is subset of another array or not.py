arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4, 5]
is_subset = True
for elem in arr1:
    if elem not in arr2:
        is_subset = False
        break
if is_subset:
    print("arr1 is a subset of arr2")
else:
    print("arr1 is not a subset of arr2")
