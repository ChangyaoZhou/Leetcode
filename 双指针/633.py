def judgeSquareSum(c):
    """
    给定一个非负整数c ，你要判断是否存在两个整数a和b，使得a^2 + b^2 = c^2。
    【双指针】分别从头尾开始搜索，直至两个指针相遇并且错过，则说明无法找到符合条件的i, j。
    i = j 是可能的，所以是while(i <= j)
    较大的指针 j 从小于c的最大的平方数对应的根开始，int向下取整，j**2一定小于c
    """
    i = 0
    j = int(pow(c, 0.5))
    while i <= j:
        if i ** 2 + j ** 2 > c:
            j -= 1
        elif i ** 2 + j ** 2 < c:
            i += 1
        elif i ** 2 + j ** 2 == c:
            return True
    return False


c = 5
print(judgeSquareSum(c))
