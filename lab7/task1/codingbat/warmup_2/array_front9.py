def array_front9(nums):
    front_len = 4
    if front_len > len(nums):
        front_len = len(nums)
        
    for i in range(front_len):
        if nums[i] == 9:
            return True
    
    return False