def get_sum(n):
    sum = 0
    while n != 0:
        m = n % 10
        sum += m * m
        n = n // 10
    return sum

# print(get_sum(8))


def isHappy(n):
    old_sum = set()
    while True:
        sum_n = get_sum(n)
        # 如果这个sum曾经出现过，说明已经陷入了无限循环了，立刻return false
        if sum_n in old_sum:
            return False
        if sum == 1:
            return True
        old_sum.add(sum_n)  # set.add(n)会将n加入到set的第一项,但是注意！！set无法通过set[0]来调用
        n = sum_n
        print(old_sum)


print(isHappy(19))
