def lengthOfLongestSubstring(s: str) -> int:
    '''
    分别找到以字符串中每一个字符开头的无重复子串，然后在遍历中比较以字符串中每一个字符开头的无重复子串长度，得到最长的无重复子串长度
    - 在每一步的操作中，我们会将左指针向右移动一格，表示 我们开始枚举下一个字符作为起始位置，
    - 然后我们可以不断地向右移动右指针，但需要保证这两个指针对应的子串中没有重复的字符。
    - 在移动结束后，这个子串就对应着 以左指针开始的，不包含重复字符的最长子串。我们记录下这个子串的长度；
    在枚举结束后，我们找到的最长的子串的长度即为答案。
    :param s:
    :return:
    '''
    if s == "":
        return 0
    window = set() # 用set来表示滑动窗口
    res = 1
    j = 0
    for i in range(len(s)):
        # 以下一位字符开头时，需要在活动窗口中去掉相对应的字符
        if i > 0:
            window.remove(s[i-1])
        #j = i
        while j < len(s):
            # 如果下一位和滑动窗口内的字母比较，如果不重复，则将当前一位的字符加入到滑动窗口中
            # 如果重复，则不会将当前一位的字符加入到滑动窗口中，也说明当前的滑动窗口已经是一个 以第i位开头的 最长无重复子串
            if s[j] in window:
                break
            window.add(s[j])
            j += 1
        res = max(res, len(window))
    return res


s = "abcabcbb"
s = "aabbcc"
s = "dvvf"
print(lengthOfLongestSubstring(s))


