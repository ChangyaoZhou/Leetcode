def canJump(nums):
    # 本题关键在于可跳的覆盖范围！！！问题可以转化为跳跃覆盖范围究竟可不可以覆盖到终点！
    # 贪心算法局部最优解：每次取最大跳跃步数（取最大覆盖范围），
    # 整体最优解：最后得到整体最大覆盖范围，看是否能到终点。
    max_range = 0
    for i in range(len(nums)):
        if max_range < i:  # 看当前的最大范围能不能到当前的第i个位置
            return False
        if i + nums[i] > max_range:  # 更新能到达的最大范围
            max_range = i + nums[i]
    if max_range >= len(nums) - 1:  # 如果cover大于等于了终点下标，直接return true就可以了
        return True
    else:
        return False


nums = [3,2,1,0,4]
# nums = [2,3,1,1,4]
print(canJump(nums))


