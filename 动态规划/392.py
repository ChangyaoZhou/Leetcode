def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    【法一】 求最长公共子序列，同1143，然后比较最长公共子序列长度是否为s的长度
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1] == m

    【法二】 以下，和1143有什么区别？？？

    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1] == m
    法三: 双指针
    """
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(s):
        return True
    else:
        return False




s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))