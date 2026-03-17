def power(number, degree):
    return number ** degree

array = input().split()
number = float(array[0])  
degree = int(array[1])
print(power(number, degree))