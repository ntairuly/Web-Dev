def end_other(a, b):
    a = a.lower()
    b = b.lower()

    if a[-len(b):] == b or b[-len(a):] == a:
        return True
    else:
        return False