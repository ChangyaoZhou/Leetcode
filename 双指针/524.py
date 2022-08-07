def is_sub_string(s, word):
    # 判断word是不是s的子字符串，e.g. s = 'abpcplea', word = 'apple'
    i = 0
    j = 0
    while i < len(s):
        if s[i] == word[j]:
            i += 1
            if j == len(word) - 1:
                return True
            else:
                j += 1
        else:
            i += 1
    return False


def findLongestWord(s, dictionary):
    """
    :type s: str
    :type dictionary: List[str]
    :rtype: str
    本题的关键是判断dictionary中的各个单词是否为s的子序列，然后在符合条件的单词中返回长度最长且位置最靠前的一个
    """
    max_len = 0
    longest_word = ''
    for word in dictionary:
        if is_sub_string(s, word):
            if len(list(word)) < max_len:
                continue
            elif len(list(word)) == max_len and word > longest_word:
                # 如果两个单词长度相同，取在dictionary中位置靠前的一个
                continue
            max_len = len(list(word))
            longest_word = word
    return longest_word


s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
print(findLongestWord(s, dictionary))


