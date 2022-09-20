n = 5
k = 10
nums = [3, 1, 5, 3, 4]
'''
i = 0
while k >= 0:
    if nums[i] != -1:
        nums[i] -= 1
        k -= 1
        if nums[i] == 0:
            nums[i] = -1
    if k == 0:
        print(i+1)
        break
    i = i + 1
    i = i % len(nums)
'''

def remove_min(nums, a):
    while True:
        try:
            idx = nums.index(a)
            nums[idx] = 1000
        except:
            return

last_min = 0
while k >= 0:
    min_a = min(nums)
    if k - (min_a - last_min) * n < 0:
        idx = k % n
        i = 0
        for j, num in enumerate(nums):
            if num != 1000:
                i += 1
            if i == idx:
                print(j+1)
                break

    k = k - (min_a - last_min) * n
    n = n - nums.count(min_a)
    remove_min(nums, min_a)
    last_min = min_a

