array_size = int(input())
array = []
array = input().split()

result = ""
array.reverse()
for i in array:
    result += i + " "

print(result)