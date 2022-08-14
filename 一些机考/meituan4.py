n = 4
nums = [4,2,2,2]
count = 0
'''
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if nums[i]-nums[j] == 2 * nums[j] - nums[k]:
                count += 1

i = 0
k = len(nums) - 1
idx_list = []
move_i = True
while i < k:
    for j in range(i+1, k):
        if nums[i] - nums[j] == 2 * nums[j] - nums[k]:
            idx_list.append((i+1, j+1, k+1))
            count += 1
    mode_i = not move_i
    if move_i:
        i += 1
    else:
        k -= 1
print(count)
print(idx_list)
'''
#count = 0
count = 0
path = []
result = []
def backtracking(nums, start_idx, count):
    if len(path) == 3 and nums[path[0]] - nums[path[1]] == 2 * nums[path[1]] - nums[path[2]]:
        result.append(path.copy())
        count += 1
        return

    for i in range(start_idx, len(nums)):
        path.append(i)
        backtracking(nums, i+1, count)
        path.pop()

backtracking(nums, 0, 0)
print(len(result))



