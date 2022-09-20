def numberOfSubarrays(nums, k):
    # dict_num中每个元素存的是，对于第i个元素之前的所有元素中可能的奇数数字的个数，及其对应的子数组数量
    # e.g.有n个奇数的子数组有dict_num[n]个
    curr_odd = 0
    count = 0
    from collections import defaultdict
    dict_num = defaultdict(int)
    # 初始化 有0个奇数的数组有1个
    dict_num[0] = 1
    for num in nums:
        if num % 2 == 1:
            curr_odd += 1 #当前元素之前奇数的个数
        count += dict_num[curr_odd - k]
        dict_num[curr_odd] += 1
    return count

nums = [1,1,2,1,1]
k = 3
print(numberOfSubarrays(nums, k))
