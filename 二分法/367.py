def isPerfectSquare(num):
    """
    给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false
    可以使用二分法，nums[i] = i*i, 看输入的num是否在nums列表里面，如果在，则为完全平方数
    """
    left = 0
    right = num
    while left <= right:
        mid = (right + left) // 2
        if num == mid * mid:
            return True
        elif num > mid * mid:
            left = mid + 1
        else:
            right = mid - 1
    return False


num = 16
print(isPerfectSquare(num))

