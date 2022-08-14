def mySqrt(x):
    """
     给你一个非负整数x ，计算并返回x的算术平方根
     类似于35题插入数字，可以按做nums[i] = i*i, 因为算术平方根只保留整数部分，即算术平方根向下取整，则求的是x插入nums之后前一位的索引，
     所以要返回的是right而不是right+1!!!

    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        if x > mid * mid:
            left = mid + 1
        elif x < mid * mid:
            right = mid - 1
        else:
            return mid
    return right
    """
    # 暴力解法, 需要时间比二分法长很多
    for i in range(x + 1):
        if x == i*i:
            return i
        elif x < i*i:
            return i - 1



x = 1
print(mySqrt(x))