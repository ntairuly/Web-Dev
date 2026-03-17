lower_border = int(input())
upper_border = int(input())
even_nums = ""

for num in range(lower_border, upper_border + 1):
    if num % 2 == 0:
        even_nums += str(num) + " "

print(even_nums)