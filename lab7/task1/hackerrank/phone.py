# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 


inputs = int(input())

for i in range(inputs):
    phone_number = input()
    if re.search("^[7, 8, 9][0-9]{9}$", phone_number):
        print("YES")
    else:
        print("NO")