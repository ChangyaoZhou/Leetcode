def maxProfit(prices):
    """
    根据prices可以得到每天的利润序列：(prices[i] - prices[i - 1]).....(prices[1] - prices[0])。
    e.g. prices = [7,1,5,3,6,4]
         从第二天起，前一天买入，今天卖出的利润依次是 profit = [-6, 4, -2, 3, -2]
    要使多次买入卖出的总利润最大，可以只取所有利润中的正利润，加和就是最大利润！！
    上面的例子中，最大利润是7，即第2天买入，第三天卖掉，第4天买入，第五天卖掉
    贪心有的时候可以把问题变得简单很多！！！就是想不到 哭了
    """
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit += max(prices[i] - prices[i-1], 0)
    if max_profit > 0:
        return max_profit
    else:
        return 0


prices = [7,1,5,3,6,4]
print(maxProfit(prices))
