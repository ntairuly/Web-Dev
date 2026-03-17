array_size = int(input())
array = []
array = input().split()
bigger_than_neighbor = 0

for i in range(array_size):
    if i > 0 and i < array_size - 1:
        if (int(array[i]) > int(array[i - 1]) 
                and int(array[i]) > int(array[i + 1])):
            bigger_than_neighbor += 1

print(bigger_than_neighbor)