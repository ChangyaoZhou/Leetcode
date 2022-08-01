'''
【01背包】
######## 原文见链接 https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-1.md
有n件物品和一个最多能背重量为w的背包。第i件物品的重量是weight[i]，得到的价值是value[i]。
***每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
背包最大重量为4。
物品为    weight value
     0     1      15
     1     3      20
     2     4      30
问背包能背的物品最大价值是多少？

同样用动态规划的五个步骤来解释。
1 【定义dp数组】
使用二维数组，即dp[i][j] 表示从下标为从0到i的物品里任意取，放进容量为j的背包，价值总和最大是多少
2 【dp初始化】
如果背包容量j为0的话，无论是选取哪些物品，背包价值总和一定为0，即dp数组的第一列，dp[i][0]全部为0。
对于dp的第一行，需要遍历所有不同的背包最大重量，
— 当物品0的重量大于当前背包最大限重j时，dp[0][j] = 0
— 当物品0的重量小于当前背包最大限重j时，表示可以装入物品0，dp[0][j] = value[0]
3 【递推公式】
'''



