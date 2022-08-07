def is_Palindrome(s, i, j):
    s_list = list(s)
    while i < j:
        if s_list[i] == s_list[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def validPalindrome(s):
    """
    先定义一个函数is_palindrome，用来判断一个string是否为palindrome
    双指针，分别从头尾开始搜索，若对应的两个字母相同，则继续找下一对，
    若对应的字母不相同，删去左边或右边的字母时，分别判断剩下的部分是否为palindrome。
    如果是palindrome,则返回true，如果剩余部分不是palindrome，则返回false.
    """
    s_list = list(s)
    i = 0
    j = len(s_list) - 1
    while i < j:
        if s_list[i] == s_list[j]:
            i += 1
            j -= 1
        elif is_Palindrome(s, i, j - 1):
            return True
        elif is_Palindrome(s, i + 1, j):
            return True
        else:
            return False
    return True

