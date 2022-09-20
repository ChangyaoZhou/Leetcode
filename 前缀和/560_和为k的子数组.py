from collections import defaultdict


def subarraySum(nums, k):
    # 建立一个default dict，存的数据类型是int，当dict中不存在某一个key时，会输出0
    # dict_sum用来存每一个前缀和的个数
    dict_sum = defaultdict(int)
    dict_sum[0] = 1
    count = 0
    curr = 0
    for num in nums:
        curr += num
        # 对于第i个元素之前的前缀和curr，查看第i个元素之前有没有加和为k的数组
        count += dict_sum[curr - k]
        dict_sum[curr] += 1
    return count

nums = [1, 2, 2, 4, 3, 2, 3, 4, 3, 5]
print(subarraySum(nums, 9))


