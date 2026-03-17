lower_border = int(input())
upper_border = int(input())
remainder = int(input())
division = int(input())
remainder_nums = ""

for num in range(lower_border, upper_border + 1):
    if num % division == remainder:
        remainder_nums += str(num) + " "

print(remainder_nums)