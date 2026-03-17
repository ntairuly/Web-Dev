array_size = int(input())
array = []
array = input().split()

answer = "NO"
for i in range(array_size):
    if i > 0:
        if (int(array[i]) > 0 and int(array[i - 1]) > 0
                or (int(array[i]) < 0 and int(array[i - 1]) < 0)):
            answer = "YES"

print(answer)