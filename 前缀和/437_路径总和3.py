class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# binary tree example
node5 = TreeNode(5)
node4 = TreeNode(6)
node3 = TreeNode(3, node5)
node2 = TreeNode(2, node4)
node1 = TreeNode(1, node2, node3)


def pathSum(root, targetSum):
    # 前缀和 回溯
    from collections import defaultdict
    #dict_num中存的是每一个可能的路径和，以及对应的个数
    dict_sum = defaultdict(int)
    dict_sum[0] = 1

    # 类似dfs，根据节点进行回溯，同时利用前缀和思想，计算路径中每一步的前缀和
    def backtracking(root, target, curr_sum):
        if not root:
            return 0
        curr_sum += root.val
        count = dict_sum[curr_sum - target]
        dict_sum[curr_sum] += 1

        if root.left:
            count += backtracking(root.left, target, curr_sum)
        if root.right:
            count += backtracking(root.right, target, curr_sum)
        # 完成一层的左右节点遍历之后，要回到上一层之前，需要将dict num还原到上一层的样子
        # 如果我们不做状态恢复，当遍历右子树时，左子树中A的信息仍会保留在map中，那此时节点6就会认为A, B都是可追溯到的节点，从而产生错误。
        # e.g. 1 -> 2 -> 3
        #        -> 2 -> 3   如果不做状态恢复，target为6的路径会有4条，实际上只有2条，路径必须是在二叉树中联通的节点组成的！！
        dict_sum[curr_sum] -= 1

        return count

    return backtracking(root, targetSum, 0)


print(pathSum(node1, 8))





