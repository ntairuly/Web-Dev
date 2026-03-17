array_size = int(input())
array = []
array = input().split()

sorted_even_array = ""
for i in range(array_size):
    if int(array[i]) % 2 == 0:
        sorted_even_array += array[i] + " "

print(sorted_even_array)