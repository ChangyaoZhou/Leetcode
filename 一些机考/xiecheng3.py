nums = [-1, 0, 1, 2, 13]
nums = [-100, 1, 2, 3, 4]
n = 5
k = 3
i = 0
j = n-1
nums.sort()
remove_num = []
max_num = nums[j]
min_num = nums[i]
if k % 2 == 0:
    while k > 0:
        remove_num.append(nums[i])
        remove_num.append(nums[j])
        i += 1
        j -= 1
        max_num = nums[j]
        min_num = nums[i]
        k -= 2
    avr = sum(remove_num) / len(remove_num)
    max_num = max(avr, max_num)
    min_num = min(avr, min_num)
    print(max_num - min_num)

else:
    avr_num = sum(nums) / len(nums)
    while (k > 1):
        remove_num.append(nums[i])
        remove_num.append(nums[j])
        i += 1
        j -= 1
        max_num = nums[j]
        min_num = nums[i]
        k -= 2
    if abs(max_num - avr_num) >= abs(min_num - avr_num):
        remove_num.append(max_num)
        max_num = nums[j - 1]
    else:
        remove_num.append(min_num)
        min_num = nums[i + 1]
    avr = sum(remove_num) / len(remove_num)
    max_num = max(avr, max_num)
    min_num = min(avr, min_num)
    print(max_num - min_num)




