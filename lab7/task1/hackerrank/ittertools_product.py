# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = product(a, b)
for i in result:
    print(i, end=" ")