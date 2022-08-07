def findMaxConsecutiveOnes(nums):
    '''
    one_count_list = []
    one_count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            one_count += 1
        else:
            one_count_list.append(one_count)
            one_count = 0
        if i == len(nums) - 1:
            one_count_list.append(one_count)
    return max(one_count_list)
    '''
    one_max, one_count = 0, 0
    for i in range(len(nums)):
        if nums[i] == 1:
            one_count += 1
        else:
            if one_count > one_max:
                one_max = one_count
            one_count = 0
        if i == len(nums) - 1:
            if one_count > one_max:
                one_max = one_count
    return one_max


nums = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums))



