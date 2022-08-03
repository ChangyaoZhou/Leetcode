def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    法一: 暴力解法 超时！！
    max = -10000
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > max:
                max = prices[j] - prices[i]
    if max < 0:
        return 0
    else:
        return max

    法二: 贪心算法
    从左向右取最小值，每次找出一个最小值后，和他后面的价格作差，找出利润最大值。
    low = 10000
    profit = -10000
    for p in prices:
        low = min(low, p)
        profit = max(profit, p - low)
    if profit < 0:
        return 0
    else:
        return profit
    法三: 动态规划
    动归五部曲:
    1 【确定dp含义】
    二维dp, dp[i][0] 表示第i天持有股票所得最多现金, dp[i][1] 表示第i天不持有股票所得最多现金
    其实一开始现金是0，那么加入第i天买入股票现金就是 -prices[i]， 这是一个负数
    2 【递推公式】
    如果第i天持有股票即dp[i][0]， 那么可以由两个状态推出来
    — 第i-1天就持有股票，那么就保持现状，所得现金就是昨天持有股票的所得现金 即：dp[i - 1][0]
    — 第i天买入股票，所得现金就是买入今天的股票后所得现金即：-prices[i]
    那么dp[i][0]应该选所得现金最大的，所以dp[i][0] = max(dp[i - 1][0], -prices[i]);

    如果第i天不持有股票即dp[i][1]， 也可以由两个状态推出来
    — 第i-1天就不持有股票，那么就保持现状，所得现金就是昨天不持有股票的所得现金 即：dp[i - 1][1]
    — 第i天卖出股票，所得现金就是按照今天股票佳价格卖出后所得现金即：prices[i] + dp[i - 1][0]
    同样dp[i][1]取最大的，dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0]);
    3 【初始化】
    dp[0][0] = -price[0], dp[0][1] = 0
    4 【遍历顺序】
    5 【举例推导dp】
    到最后一天为止，不持有股票时拥有的最大现金数就是最大利润
    """
    dp = [[0, 0] for _ in range(len(prices))]
    dp[0][0] = -prices[0]
    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], -prices[i])
        dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])
    return dp[-1][-1]




prices = [7,1,5,3,6,4]
print(maxProfit(prices))