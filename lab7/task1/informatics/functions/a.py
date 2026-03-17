def min(num1, num2, num3, num4):
    array = [num1, num2, num3, num4]
    array.sort()
    print(array[0])

array = input().split()
num1 = int(array[0])
num2 = int(array[1])
num3 = int(array[2])
num4 = int(array[3])
min(num1, num2, num3, num4)