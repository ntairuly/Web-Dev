def xor (bool1, bool2):
    if bool1 == bool2:
        return 0
    else:
        return 1

array = input().split()
bool1 = int(array[0])
bool2 = int(array[1])
print(xor(bool1, bool2))