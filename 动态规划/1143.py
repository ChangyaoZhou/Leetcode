# import numpy as np
def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    *** 本题中可以删除元素，但是不能改变顺序！！
    dp[i][j]：长度为i - 1的字符串text1与长度为j - 1的字符串text2的最长公共子序列为dp[i][j]
    e.g. text1 = "abcde", text2 = "ace"，则dp是6x4的列表
    dp:
          a  c  e
       0  0  0  0
    a  0  1  1  1
    b  0  1  1  1
    c  0  1  2  2
    d  0  1  2  2
    e  0  1  2  3
    【递推公式】
    — text1[i - 1] = text2[j - 1], 则 dp[i][j] = dp[i - 1][j - 1] + 1
    — 若不相等，dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    *** 因为可以删除元素，所以dp[i][j]左上区域中的最长公共子序列长度可以保留
    而且，不需要用max_len来记录最大长度，dp从左上到右下的值是递增的，返回dp[-1][-1]即可
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp)
    return dp[-1][-1]


text1 = "abcde"
text2 = "acebcde"
print(longestCommonSubsequence(text1, text2))