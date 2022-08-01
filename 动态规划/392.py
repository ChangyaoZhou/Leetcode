def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    法一: 求最长公共子序列，同1143，然后比较最长公共子序列长度是否为s的长度
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1] == m
    法二:
    建立dp，dp[i][j]表示在t中存在的
    """
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1] == m

s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))