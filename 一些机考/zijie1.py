nums = ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1']
max_len = 1
num_len = 1
for i in range(1, len(nums)):
    if int(nums[i]) + int(nums[i-1]) == 1:
        num_len += 1
    else:
        num_len = 1
    max_len = max(max_len, num_len)
print(max_len)


