number = input()
number = number[::-1]
reversed_num = ""

for i in number:
    if i == '0' and len(reversed_num) == 0:
        continue
    else:
        reversed_num += i

print(reversed_num)