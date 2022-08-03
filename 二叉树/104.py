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


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    que = [root]
    max_depth = 0
    while que:
        max_depth += 1
        size = len(que)
        for i in range(size):
            cur = que.pop(0)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
    return max_depth


print(maxDepth(node1))


