number = int(input())
min_divisor = 1

for i in range(2, number + 1):
    if number % i == 0:
        min_divisor = i
        break

print(min_divisor)