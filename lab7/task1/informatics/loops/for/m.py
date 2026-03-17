sum = 0
entry_num = int(input())

for i in range(0, entry_num):
    number = int(input())
    if number == 0:
        sum += 1

print(sum)