lower_border = int(input())
upper_border = int(input())
square_nums = ""

for num in range(lower_border, upper_border + 1):
    if num**0.5 % int(num**0.5) == 0:
        square_nums += str(num) + " "

print(square_nums)