nums = [3,2,2,1,20,1,1,3]
len_nums = 8
x = 10

nums_sum = [0, nums[0]]
nums_sum_reverse = [0, nums[-1]]
for i in range(1, len_nums):
    if nums_sum[i-1] + nums[i] > x:
        break
    nums_sum.append(nums_sum[-1] + nums[i])
#print(nums_sum)

for i in range(len_nums-2, -1, -1):
    if nums_sum_reverse[-1] + nums[i] > x:
        break
    nums_sum_reverse.append(nums_sum_reverse[-1] + nums[i])
#print(nums_sum_reverse)

min_count = 1000
for i in range(len(nums_sum)):
    for j in range(len(nums_sum_reverse)):
        if nums_sum[i] + nums_sum_reverse[j] == x:
            min_count = min(min_count, i+j)
if min_count == 1000:
    print(-1)
else:
    print(min_count)