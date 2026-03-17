def make_bricks(small, big, goal):
    if small + big * 5 < goal:
        return False
    elif goal % 5 > small:
        return False
    else:
        return True