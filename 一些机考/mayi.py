nums = [3, 2, 4]
n = 3

i = 0
count = 0
while(i < n-1):
    i += 1
    if nums[i] > nums[i-1]:
        continue
    else:
        count += nums[i-1] - nums[i] + 1
print(count)

dp = [0 for _ in range(n)]
for i in range(1, n):
    if nums[i] > nums[i-1] + dp[i-1]:
        continue
    else:
        dp[i] = nums[i-1] + dp[i-1] + 1 - nums[i]
print(max(dp))
