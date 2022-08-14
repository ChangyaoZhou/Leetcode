def isAnagram(s, t):
    """
    若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词
    字母字符串和数字之间的转化
    chr(65) = 'A', ord('A') = 65， ord('a') = 65

    出现“小写字符”，“出现频率”，就可以考虑用【哈希表】！！
    本题中哈希表用来记录每个字母的出现次数
    """
    letter_count = [0] * 26
    for i in s:
        # 不用管每个字母对应的数字是几，求每个字母相对于第一个字母a的位置就好了
        idx = ord(i) - ord('a')
        letter_count[idx] += 1
    for i in t:
        idx = ord(i) - ord('a')
        letter_count[idx] -= 1
    # letter count数组如果有的元素不为零0，说明字符串s和t一定是谁多了字符或者谁少了字符
    for count in letter_count:
        if count != 0:
            return False
    return True


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
