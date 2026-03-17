array_size = int(input())
array = input().split()

count = 0
for i in range(1, array_size):
    if int(array[i]) > int(array[i - 1]):
        count += 1

print(count)