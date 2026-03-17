def common_end(a, b):
    if len(a) >= 1 and len(b) >= 1:
        return a[0] == b[0] or a[-1] == b[-1]
    return False