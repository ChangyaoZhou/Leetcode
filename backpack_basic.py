'''
【01背包】
有n件物品和一个最多能背重量为w的背包。第i件物品的重量是weight[i]，得到的价值是value[i]。
***每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
背包最大重量为4。
物品为    weight value
     0     1      15
     1     3      20
     2     4      30
问背包能背的物品最大价值是多少？
'''

def backpack_01(weights, values, bag_size):
    # initialization
    dp = [[0] * (bag_size + 1) for _ in values]
    for i in range(bag_size + 1):
        if i >= weights[0]:
            dp[0][i] = values[0]
        else:
            dp[0][i] = 0
    for i in range(1, len(weights)): # i表示每个物品
        for j in range(1, bag_size + 1): # j表示各个背包的最大限重
            if weights[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                tmp_value = dp[i - 1][j - weights[i]] + values[i]
                dp[i][j] = max(dp[i - 1][j], tmp_value)
    return dp[-1][-1]


weights = [1, 3, 4]
values = [15, 20, 30]
bag_size = 4
print(backpack_01(weights, values, bag_size))









