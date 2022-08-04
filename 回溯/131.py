def is_palindrome(s, start, end):

    i = start
    j = end
    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


'''
s = 'babac'
print(is_palindrome(s, 1, 3))
print(s[1:4])
'''

def partition(s):
    '''
    递归用来纵向遍历，for循环用来横向遍历
    全局变量数组path存放切割后回文的子串，二维数组result存放结果集
    本题递归函数参数还需要startIndex，因为切割过的地方，不能重复切割
    ** 本题和77组合问题差不多，只是多了一个判断是否为回文的环节，
    另外，切割可以用取s[start_index: i+1]来表示
    '''
    result = []
    palindrome = []

    def backtracking(s, start_index):
        if start_index == len(s):  # 当切割到s的最后一位时，代表切割完成，将当前的切割组合palindrome存入result
            result.append(palindrome.copy())
            return

        # backtracking
        for i in range(start_index, len(s)):  # 循环代表遍历当前层的所有可能性
            if is_palindrome(s, start_index, i):  # 如果要切割的部分是回文，则存下来，进入下一层
                palindrome.append(s[start_index: i+1])
                backtracking(s, i+1)  # 每一次的backtracking都是进入下一层
                palindrome.pop()

    backtracking(s, 0)
    return result


s = "aab"
print(partition(s))



