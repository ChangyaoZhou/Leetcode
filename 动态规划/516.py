def longestPalindromeSubseq(s):
    """
    【dp定义】
    dp[i][j]：字符串s在[i, j]范围内含有的最长的回文子序列的长度为dp[i][j]，不一定就是s[i:j+1],其中也可进行删减。
    【初始化】
    由dp的定义可以知道dp的下三角值都是0，当i与j相同，那么dp[i][j]一定是等于1的，即：一个字符的回文子序列长度就是1。
    【递推公式】
    e.g. s = " b    a    b   c   b       a   f"
                    i    i+1     j-1     i
    如果s[i]与s[j]相同，那么dp[i][j] = dp[i + 1][j - 1] + 2;
    e.g. s = " b    d    b   c   c       b   f"
                    i    i+1     j-1     j
    如果s[i]与s[j]不相同，那么看分别在左右去掉一位时，最长的回文子序列
    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    dp[i][j - 1] = 2, dp[i + 1][j] = 4

    e.g. s = b   b   b   a   b
        b   1   2   3   3   4
        b   0   1   2   2   3
        b   0   0   1   1   3
        a   0   0   0   1   1
        b   0   0   0   0   1

    【遍历顺序】
    因为计算dp[i][j]时需要用到dp[i][j - 1]，dp[i + 1][j]，所以从下到上，从左到右遍历

    """
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    print(dp)
    for i in range(len(s)-2, -1, -1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    print(dp)
    return dp[0][-1]


s = "bbbab"
print(longestPalindromeSubseq(s))
