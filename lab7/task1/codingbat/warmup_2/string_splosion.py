def string_splosion(str):
    result = ""
    for i in range(len(str)):
        for j in range(i + 1):
            result += str[j]
    return result