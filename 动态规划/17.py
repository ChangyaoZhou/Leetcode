def letterCombinations(digits):
    '''
    在本题中，横向循环遍历的是每个数字对应的3/4个字母
    纵向遍历的深度，是digits输入的长度
    :param digits:
    :return:
    '''
    letter_map = {'2': 'abc',
                  '3': 'def',
                  '4': 'ghi',
                  '5': 'jkl',
                  '6': 'mno',
                  '7': 'pqrs',
                  '8': 'tuv',
                  '9': 'wxyz'}
    # 初始化
    result = []
    answer = ''

    if digits == '':
        return []

    def backtracking(digits, index, answer):
        # index表示当前进行到第几层，处理到digits中的第几个字母
        if len(answer) == len(digits):  # 当answer和digits长度相同，代表已经进行到最后一层了
            result.append(answer)
            return

        letters = letter_map[digits[index]]  # 从letter map中提取digits中每个数字对应的字母序列
        for letter in letters:
            backtracking(digits, index+1, answer + letter) #  递归，注意index+1，一下层要处理下一个数字了

    backtracking(digits, 0, answer)
    return result

print(letterCombinations('23'))
