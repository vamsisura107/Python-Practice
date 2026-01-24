num=int(input("Enter a number: "))
digits=str(num)
num_digits=len(digits)
total=0
for d in digits:
    total += int(d)**num_digits
if total==num:
    print("The number is an anagram.")
else:

    print("The number is not an anagram.")