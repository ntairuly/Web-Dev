# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar


date = input().split()

day_num = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
print(calendar.day_name[day_num].upper())