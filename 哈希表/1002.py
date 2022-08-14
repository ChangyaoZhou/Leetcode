def commonChars(words):
    """
    *** 本题中如果有重复的字母，也要输出！！！
    e.g. words = ["bella","label","roller"] 每个单词中都有一个e，两个l，所以要输出["e","l","l"]

    出现“小写字符”，“出现频率”，就可以考虑用【哈希表】！！
    本题中哈希表用来记录每个字母的出现次数，

    整体思路就是统计出搜索字符串里26个字符的出现的频率，然后取每个字符频率最小值，
    若最小值为0，说明words中有的单词不含有这个字母，
    若最小值为1，说明words中每个单词都至少含有一个该字母  --> 输出一个该字母
    若最小值为2，说明words中每个单词都至少含有两个该字母  --> 输出两个该字母
    


    """
    result = []
    # 用来统计所有字符串里字符出现的最小频率
    hash_min = [0] * 26
    # 先记录第一个单词中各个字母的出现频率
    for letter in words[0]:
        hash_min[ord(letter) - ord('a')] += 1
    # 接下来统计其他单词中各个字母的出现频率，
    for word in words:
        hash_other = [0] * 26
        for letter in word:
            hash_other[ord(letter) - ord('a')] += 1
        for k in range(26):
            hash_min[k] = min(hash_min[k], hash_other[k])
    for k in range(26):
        if hash_min[k] != 0:
            result.extend([chr(ord('a') + k)] * hash_min[k])
    return result


words = ["bella", "label", "roller"]
print(commonChars(words))

