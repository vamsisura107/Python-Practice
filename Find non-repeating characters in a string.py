s = input("Enter a string: ")

print("Non-repeating characters:")

for ch in s:
    if s.count(ch) == 1:
        print(ch, end=" ")
