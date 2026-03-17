array_size = int(input())
array = []
array = input().split()

pos_elements = 0
for i in range(array_size):
    if int(array[i]) > 0:
        pos_elements += 1

print(pos_elements)