s = input("Enter a string: ")

result = ""

for ch in s:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch   # keep digits and special characters unchanged

print("Toggled string:", result)
