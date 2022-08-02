class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# define a binary tree
node6 = TreeNode(9)
node5 = TreeNode(3)
node4 = TreeNode(5)
node3 = TreeNode(2, None, node6)
node2 = TreeNode(3, node4, node5)
node1 = TreeNode(1, node2, node3)


def largestValues(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    对于每一层的节点，求最大值存下来
    """
    if root == None:
        return []
    from collections import deque
    que = deque([root])
    max_result = []
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
        max_result.append(max(nodes_val))
    return max_result


print(largestValues(node1))

