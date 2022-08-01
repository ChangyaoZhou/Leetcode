#problem 524

def findLongestWord(s, dictionary):
    """
    :type s: str
    :type dictionary: List[str]
    :rtype: str
    """
    max_len = 0
    longest_word = ''
    for word in dictionary:
        if is_sub_string(s, word):
            if len(list(word)) < max_len:
                continue
            elif len(list(word)) == max_len and word > longest_word:
                continue
            max_len = len(list(word))
            longest_word = word
    return longest_word



def is_sub_string(s:str, word:str):
    i = 0
    j = 0
    while i < len(s):
        if s[i] == word[j]:
            i+=1
            if j == len(word) - 1:
                return True
            else:
                j+=1
        else:
            i+=1
    return False


print(is_sub_string('aaapleeeee', 'apple'))
s = "abce"
dictionary = ["ale","abe","abc","plea"]
longest_word = findLongestWord(s, dictionary)
print(longest_word)