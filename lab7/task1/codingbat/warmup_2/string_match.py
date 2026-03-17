def string_match(a, b):
    count = 0
    sub_2a = ""
    sub_2b = ""

    for i in range(len(a) - 1):
        sub_2a = a[i:i + 2]
        sub_2b = b[i:i + 2]
        if sub_2a == sub_2b:
            count += 1

    return count