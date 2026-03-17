def last2(str):
    if len(str) < 2:
        return 0
    
    last2_str = str[len(str) - 2: len(str)]
    count = 0

    for i in range(len(str) - 2):
        sub_str = str[i:i + 2]
        if sub_str == last2_str:
            count += 1
            
    return count