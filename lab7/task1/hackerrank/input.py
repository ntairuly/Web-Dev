# Enter your code here. Read input from STDIN. Print output to STDOUT
x, answer = map(int, input().split())
expression = input()
print(eval(expression) == answer)
