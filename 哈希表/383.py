def canConstruct(ransomNote, magazine):
    """
    本题类似242题，先统计magazine中各个字母出现的次数，然后看够不够组成ransomnote中的单词

    本题判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成，但是这里需要注意两点。
    第一点“为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思”  这里说明杂志里面的字母【不可重复使用】，但是和顺序无关。
    第二点 “你可以假设两个字符串均只含有小写字母。” 说明只有小写字母，这一点很重要
    """
    hash = [0] * 26
    for letter in magazine:
        hash[ord(letter) - ord('a')] += 1

    for letter in ransomNote:
        hash[ord(letter) - ord('a')] -= 1
        if hash[ord(letter) - ord('a')] < 0:
            return False
    return True


ransomNote = "aa"
magazine = "ababdf"
print(canConstruct(ransomNote, magazine))

