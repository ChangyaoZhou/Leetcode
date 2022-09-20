def subarraysDivByK(nums, k):
    # dict中存的是所有前缀和除以k可能的余数，以及其对应的个数
    # 如果前后两个前缀和除以k的余数相同，则说明他们之间的子数组，元素加和可以被k整除
    from collections import defaultdict
    curr = 0
    count = 0
    dict_num = defaultdict(int)
    dict_num[0] = 1
    for num in nums:
        curr += num
        curr_remain = curr % k
        count += dict_num[curr_remain]
        dict_num[curr_remain] += 1
    return count


nums = [4,5,0,-2,-3,1]
k = 5
print(subarraysDivByK(nums, k))

