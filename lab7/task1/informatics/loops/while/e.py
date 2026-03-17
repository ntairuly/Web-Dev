number = int(input())
power = 0
two_power = 1

while number > two_power:
    power += 1
    two_power *= 2

print(power)