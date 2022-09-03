'''
二叉搜索树是一个有序树：
若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
它的左、右子树也分别为二叉搜索树
'''

############## 详细解析见链接！！！！！ ####################
# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0096.%E4%B8%8D%E5%90%8C%E7%9A%84%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.md
def numTrees(n):
    """
    :type n: int
    :rtype: int
    动态规划五部曲:
    1【确定dp数组的含义】 dp[i] ： 1到i为节点组成的二叉搜索树的个数为dp[i]
    2【确定递推公式】 dp[i] += dp[j - 1] * dp[i - j]; ，j-1 为j为头结点左子树节点数量，i-j 为以j为头结点右子树节点数量
    e.g. i = 4时  总节点数i=4 | 头节点序号j | 左子树节点数 | 右子树节点数
                     4      |    1     |     0     |      3
                     4      |    2     |     1     |      2
                     4      |    3     |     2     |      1
                     4      |    4     |     3     |      0
    3【dp数组如何初始化】i = 0时，dp[0]存为1，为了方便后面乘法计算， dp[1} = 1, dp[2] = 2
    4【确定遍历顺序
    首先一定是遍历节点数i，每个循环i里面每一个数作为头结点的状态，用j来遍历。
    5【举例推导dp数组】
    """
    if n < 3:
        return n
    dp = []
    dp.append(1)
    dp.append(1)
    dp.append(2)
    for i in range(3, n + 1):
        num_tree = 0
        for j in range(1, i + 1):
            num_tree += dp[j - 1] * dp[i - j]
        dp.append(num_tree)
    return dp[-1]


n = 5
print(numTrees(n))
