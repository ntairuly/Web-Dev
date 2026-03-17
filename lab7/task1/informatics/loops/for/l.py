binary_number = input()
number = 0
power = 0
binary_number = binary_number[::-1]

for i in binary_number:
    number += int(i) * 2**power
    power += 1

print(number)