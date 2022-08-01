def integerBreak(n):
    """
    :type n: int
    :rtype: int
    建立一个dp list，dp[i]表示分拆数字i+1，可以得到的最大乘积
    对于每一个数字i，需要另一个循环，对于i之前的每一个数字j都有一个对应的最大乘积，
    递推公式：dp[i] = max((i - j) * dp[j - 1], (i - j) * j)
    j * (i - j) 是单纯的把整数拆分为两个数相乘，而(i - j) * dp[j - 1]是拆分成两个以及两个以上的个数相乘
    我们把这些乘积存在 product_list中, product_list的最大值即为dp[i]
    e.g. dp = [1, 1, 2, 4, 6]

    """
    dp = []
    dp.append(1)
    dp.append(1)
    for i in range(3, n+1): # i为要拆分的数字
        product_list = [max((i - j) * dp[j - 1], (i - j) * j) for j in range(1, i)]
        dp.append(max(product_list))
    return dp[-1]

n = 10
print(integerBreak(n))