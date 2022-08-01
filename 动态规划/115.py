def numDistinct(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    dp[i][j]：以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为dp[i][j]
    """
    m = len(s)
    n = len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

