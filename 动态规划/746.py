def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    cost长度为n，每一项为离开第i级台阶所需要的花费，(一步可以迈一个台阶或两个台阶)
    e.g. cost = [5, 15, 10]， 5为从第0级台阶到第1级台阶，或从第0级台阶到第2级台阶所需的花费
    建立一个dp，长度为n+1，dp[i]代表到达第i级台阶所需要的最少花费，
    e.g.
    第0级: 0
    第1级: 0(因为也可以从第一级台阶开始)
    i>2时: 一步可以迈一个台阶或两个台阶，所以对于第i级台阶，可能是从第i级迈上来的，或者从可能是从第i-1级迈上来的
    dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1]))
    """
    dp = []
    dp.append(0)
    dp.append(0)
    for i in range(2, len(cost) + 1):
        dp.append(min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1]))
    return dp

cost = [1,100,1,1,1,100,1,1,100,1]
cost = [10, 15, 20]
print(minCostClimbingStairs(cost))