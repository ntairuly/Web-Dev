number = int(input())
while number > 1:
    number /= 2
    
if int(number) == number:
    print("YES")
else:
    print("NO")
