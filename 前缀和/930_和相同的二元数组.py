#和560没有任何区别，只是换成二元数组
def numSubarraysWithSum(nums, goal):
    from collections import defaultdict
    dict_sum = defaultdict(int)
    dict_sum[0] = 1
    count = 0
    curr = 0
    for num in nums:
        curr += num
        count += dict_sum[curr - goal]
        dict_sum[curr] += 1
    return count

nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSum(nums, goal))