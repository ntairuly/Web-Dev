number = int(input())
count = 0

for i in range(1, int(number**0.5) + 1):
    if number % i == 0:
        count += 2
        if i * i == number:
            count -= 1

print(count)