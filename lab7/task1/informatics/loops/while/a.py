max_number = int(input())
number = 1

while True:
    if number**2 > max_number:
        break
    else:
        print(number**2)
        number = number+1
