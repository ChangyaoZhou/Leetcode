n = 6
k = 3
nums = [1, 3, 1, 5, 3, 1, 5, 5, 5]
nums.sort()
first, first_pos, res = nums[0], 0, 0
'''
for i in range(1, n):
    if nums[i] - first > k:
        res = max(res, i - first_pos)
        first = nums[i]
        first_pos = i
print(res)
'''
for i in range(0, n):
    for j in range(i+1, n+1):
        len_max = n - i
        sub_num = nums[i:j]
        if sub_num[-1] - sub_num[0] > k:
            len_max = j-i-1
            break
    res = max(res, len_max)
print(res)





if nums[-1] - nums[0] <= k:
    print(n)
from collections import defaultdict
nums_count = defaultdict(int)
for num in nums:
    nums_count[num] += 1

res = n
while len(nums) > 0:
    if nums[-1] - nums[0] <= k:
        print(res)
        break
    n_max = nums_count[nums[-1]]
    n_min = nums_count[nums[0]]
    if n_min >= n_max:
        nums = nums[:len(nums) - n_max]
        res -= n_max
    else:
        nums = nums[n_min - 1:]
        res -= n_min



