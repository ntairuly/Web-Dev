def sum13(nums):
    sum = 0
    skip = False

    for num in nums:
        if num == 13:
            skip = True
        elif skip:
            skip = False
        else:
            sum += num

    return sum