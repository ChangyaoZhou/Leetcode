n, m = 5, 3
nums = [2, 1, 5, 3, 2]

def minus_nums(nums, m):
    n = len(nums)
    max_val = max(nums)
    max_idx = nums.index(max_val)
    if nums[max_idx-1] == 0 and nums[max_idx+1] == 0:
        return
    if nums[max_idx-1] < nums[max_idx+1] or nums[max_idx-1] == 0 or max_idx < m - 1:
        for i in range(m):
            nums[max_idx + i] -= 1
        minus_nums(nums, m)
    if nums[max_idx-1] > nums[max_idx+1] or nums[max_idx+1] == 0 or max_idx > n - m:
        for i in range(m):
            nums[max_idx - i] -= 1
        minus_nums(nums, m)
    #if nums[max_idx-1] == nums[max_idx+1]:



minus_nums(nums, m)
print(nums)
