number = int(input())
divisor =""

for i in range(1, number + 1):
    if number % i == 0:
        divisor += str(i) + " "

print(divisor)