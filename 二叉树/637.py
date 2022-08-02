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


def averageOfLevels(root):
    """
    :type root: TreeNode
    :rtype: List[float]
    对于每一层的节点，求平均值存下来
    """
    from collections import deque
    que = deque([root])
    avr_result = []
    while que:
        size = len(que)
        nodes_val = []
        for i in range(size):
            cur = que.popleft()
            nodes_val.append(cur.val)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
        avr = sum(nodes_val) / len(nodes_val)
        avr_result.append(float(avr))
    return avr_result

print(averageOfLevels(node1))

