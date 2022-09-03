def countSubstrings(s):
    """
     dp[i][j]表示闭区间范围[i,j]（注意是左闭右闭）的子串是否是回文子串，1为有，0为没有
    注意！！回文子串必须是连续的！ s = "bbbab","bbbb"不是回文子串，而是回文子序列
    因为是回文子串，闭区间范围[i,j]对应的长度一定(j-i+1),所以我们没必要在dp中记录字串的长度，只需要记录是否是子串

    本题同5题，只是不用记录最长字串，每次判断一个子串为回文后，count+1即可
    """

    count = 0
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
        count += 1

    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                if abs(i-j) == 1:
                    dp[i][j] = 1
                    count += 1
                else:
                    dp[i][j] = dp[i+1][j-1]
                    count += dp[i][j]
            else:
                dp[i][j] = 0
    return count


s = "abbc"
print(countSubstrings(s))


