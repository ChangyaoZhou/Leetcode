'''
回溯法也可以叫做回溯搜索法，它是一种搜索的方式。
回溯是递归的副产品，只要有递归就会有回溯。
虽然回溯法很难，很不好理解，但是回溯法并不是什么高效的算法。
回溯法解决的问题都可以抽象为树形结构，是的，我指的是所有回溯法的问题都可以抽象为树形结构！
【回溯三部曲】
1 回溯函数模板返回值以及参数
2 回溯函数终止条件
3 回溯搜索的遍历过程
【回溯代码的模板】
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}
典型的回溯问题: 77 组合问题
'''


def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    回溯法解决的问题都可以抽象为树形结构（N叉树），在本题中n是树的宽度，k是树的深度，
    回溯法的搜索过程就是一个树型结构的遍历过程，在如下图中，可以看出for循环用来横向遍历，递归的过程是纵向遍历。
    """
    results = []
    path = []

    def backtracking(n, k, start_idx):
        '''
        退出一个 backtracking函数有两种可能
        1 完成了循环，返回到上一层的 backtraking中
        2 达到了最大深度，返回到上一层节点
        '''
        # 递归终止条件
        if len(path) == k:  # len达到k代表达到了最大深度
            results.append(path[:])
            return
        # for i in range(start_idx, n + 1):  # 完成这个循环代表横向遍历了当前层的所有节点
        tmp = k - len(path)
        for i in range(start_idx, n - tmp + 2):
            path.append(i)
            backtracking(n, k, i+1)
            path.pop() # 删除当前path中的最后一项，返回到上一层的节点

    backtracking(n, k, 1)
    return results

'''
从上面的循环中我可以看出，存在一些不必要的循环
e.g.计算combine(5, 4)时，第一位依次选择1，2，3，4，5。
但是实际上，因为要从5个数中选择4个，第一位选择3，4，5时，后面的数字已经不够4个了，所以没必要在进行这三个循环。
所以需要【剪枝】！！！
如何实现剪枝呢？？ 改变递归中每一层的for循环的结束位置！！！
对于每一层的循环，之前for i in range(start_idx, n + 1)从start_idx循环到最后一个数，
先求tmp = k - len(path), tmp是在要选的k个数中还差几个，
n-tmp+1表示在n个数中要按顺序取tmp个数字，起始为止最大只能是n-tmp+1， 如果从更大的数开始，则后面剩余的数字不够tmp个
剪枝后循环范围为 [start_idx, start_idx+1, ..., n-tmp+1]
所以代码中每一层循环为 for i in range(start_idx, n-tmp+2)

***剪枝之后可以大大减小运行时间，尤其是n和k比较接近时！
'''

print(combine(5, 3))



