class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# define a binary tree
node4 = TreeNode(15)
node5 = TreeNode(7)
node3 = TreeNode(20, node4, node5)
node2 = TreeNode(9)
node1 = TreeNode(3, node2, node3)

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    层序遍历一个二叉树。就是从左到右一层一层的去遍历二叉树。
    广度优先遍历，类似DFS
    需要用到队列来实现，先进先出，import collecitons.deque

    法一:迭代
    if root == None:
        return []
    from collections import deque
    que = deque([root])
    results = []
    while que:  # 每次循环对应二叉树的每一层
        size = len(que)
        result = []
        for i in range(size):  # 遍历该层的每一个节点
            cur = que.popleft() # 从队列的左侧出一个元素
            result.append(cur.val)
            if cur.left:  # 添加当前节点位于下一层的左节点
                que.append(cur.left)
            if cur.right:  # 添加当前节点位于下一层的右节点
                que.append(cur.right)
        results.append(result)
    return results
    法二:递归
    """
    results = []

    def helper(root, depth):  # 用于存下当前节点的值，并继续进入和当前节点连接的子节点
        if root == None:
            return []
        if len(results) == depth:  # 判断是否需要添加一层的result
            results.append([])
        results[depth].append(root.val)
        # print(results)
        if root.left:
            helper(root.left, depth + 1)
        if root.right:
            helper(root.right, depth + 1)
    helper(root, 0)
    return results



print(levelOrder(node1))




