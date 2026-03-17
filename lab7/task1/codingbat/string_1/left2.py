def left2(str):
    if len(str) >= 2:
        return str[2:len(str)] + str[0:2]
    return str