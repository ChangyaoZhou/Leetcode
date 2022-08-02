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


def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    层序遍历同102，只需要最后将results顺序反转
    """
    if root == None:
        return []
    from collections import deque
    que = deque([root])
    results = []
    while que:  # 每次循环对应二叉树的每一层
        size = len(que)
        result = []
        for i in range(size):  # 遍历该层的每一个节点
            cur = que.popleft()  # 从队列的左侧出一个元素
            result.append(cur.val)
            if cur.left:  # 添加当前节点位于下一层的左节点
                que.append(cur.left)
            if cur.right:  # 添加当前节点位于下一层的右节点
                que.append(cur.right)
        results.append(result)
    return results[::-1]  # result.reverse()


print(levelOrderBottom(node1))
