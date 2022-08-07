def reverseVowels(s):
    """
    双指针，分别从头尾开始搜索，如果当前位置是元音，则指针保持不动，等待另一个指针也找到元音。
    如果当前位置不是元音，则进行向前/后移动一格。当两个指针都找到元音，则进行交换，且两个指针都移动一格。
    直至两个指针相遇，则说明没有可以配对的元音。
    ***可能存在中间的单个元音，e.g. iloveyou -> uloveyoi，所以i不能等于j，i等于j时就可以停止循环。
    """
    s_list = list(s)
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    i = 0
    j = len(s_list) - 1
    # vowel_pair = []
    while i < j:
        if s_list[i] not in vowel:
            i += 1
        if s_list[j] not in vowel:
            j -= 1
        if s_list[i] in vowel and s_list[j] in vowel:
            # print(i,j)
            emp = s_list[i]
            s_list[i] = s_list[j]
            s_list[j] = emp
            # vowel_pair.append((s_list[i], s_list[j]))
            i += 1
            j -= 1
    return "".join(s_list)


s = "leetcode"
print(reverseVowels(s))

