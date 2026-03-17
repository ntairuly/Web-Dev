command_number = int(input())
arr = []

for i in range(command_number):
    command = input().split()
    for i in range(len(command)):
        if i != 0:
            command[i] = int(command[i])        
    
    if len(command) == 3:
        if command[0].lower() == "insert":
            arr.insert(command[1], command[2])
        else:
            print("Unknown command")
    
    elif len(command) == 2:
        if command[0].lower() == "remove":
            arr.remove(command[1])
        elif command[0].lower() == "append":
            arr.append(command[1])
        else:
            print("Unknown command")
    
    elif len(command) == 1:
        if command[0].lower() == "print":
            print(arr)
        elif command[0].lower() == "sort":
            arr.sort()
        elif command[0].lower() == "pop":
            arr.pop()
        elif command[0].lower() == "reverse":
            arr.reverse()
        else:
            print("Unknown command")
            
    else:
        print("Unknown command")