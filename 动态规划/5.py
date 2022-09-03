def longestPalindrome(s):
    """
    【dp定义】
    dp[i][j]表示闭区间范围[i,j]（注意是左闭右闭）的子串是否是回文子串，1为有，0为没有
    注意！！回文子串必须是连续的！ s = "bbbab","bbbb"不是回文子串，而是回文子序列
    因为是回文子串，闭区间范围[i,j]对应的长度一定(j-i+1),所以我们没必要在dp中记录字串的长度，只需要记录是否是子串

    【初始化】
    由dp的定义可以知道dp的下三角值都是0，当i与j相同，那么dp[i][j]一定是等于1的，即：一个字符的回文子序列长度就是1。

    【递推公式】
    ** 当s[i]与s[j]不相等，那没啥好说的了，dp[i][j]一定是false。
    ** 当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况
    情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
    情况二：下标i 与 j相差为1，例如aa，也是回文子串
    情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，我们看i到j区间是不是回文子串就看aba是不是回文就可以了，
    那么aba的区间就是 i+1 与 j-1区间，这个区间是不是回文就看dp[i + 1][j - 1]是否为true。

    每次判断一个子串为回文后，把他和max_len作比较，更新最长回文子串

    【遍历顺序】
    因为计算dp[i][j]时需要用到dp[i][j - 1]，dp[i + 1][j]，所以从下到上，从左到右遍历
    """
    if len(s) == 1:
        return s
    longest_str = s[0]
    max_len = 1
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    for i in range(len(s) - 2, -1, -1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                if abs(i-j) == 1:
                    dp[i][j] = 1
                    if max_len < 2:
                        longest_str = s[i:j+1]
                        max_len = 2
                elif dp[i+1][j-1]:
                    dp[i][j] = dp[i+1][j-1]
                    if max_len < j-i+1:
                        longest_str = s[i:j + 1]
                        max_len = j-i+1
            else:
                dp[i][j] = 0

    print(dp)
    return longest_str

s = "aacabdkacaa"
print(longestPalindrome(s))

