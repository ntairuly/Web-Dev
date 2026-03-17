number = input()
finding_digit = input()
found = 0

for i in number:
    if i == finding_digit:
        found += 1

print(found)