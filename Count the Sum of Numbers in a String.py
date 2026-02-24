v = "kdjbd22@#$%^&*("
total = 0

for i in v:
    if i.isdigit(): 
        total += int(i)  

print(total)
