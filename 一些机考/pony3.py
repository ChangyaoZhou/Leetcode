input_str = 'pypypoonyony'
target = 'pony'
n = 12
if len(input_str) < len(target):
    print(0)
dp = [[0 for _ in range(n)] for _ in range(4)]
if target[0] == input_str[0]:
    dp[0][0] = 1
for j in range(1, n):
    if target[0] == input_str[j]:
        dp[0][j] = dp[0][j - 1] + 1
    else:
        dp[0][j] = dp[0][j - 1]
for i in range(1, 4):
    for j in range(n):
        if target[i] == input_str[j]:
            dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j])
        else:
            dp[i][j] = dp[i][j-1]

print(dp[-1][-1])