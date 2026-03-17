n = int(input())
set1 = set(map(int, input().split()))
command_number = int(input())

for i in range(command_number):
    command = input().split()
    for i in range(len(command)):
        if i != 0:
            command[i] = int(command[i])        
    
    if len(command) == 2:
        if command[0].lower() == "remove":
            set1.remove(command[1])
        elif command[0].lower() == "discard":
            set1.discard(command[1])

    if len(command) == 1:
        if command[0].lower() == "pop":
            set1.pop()
    
sum = 0            
for i in set1:
     sum += i
print(sum)