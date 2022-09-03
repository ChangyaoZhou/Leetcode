class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# define a node tree
'''
node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(20, node1, node2)
node4 = TreeNode(9)
node5 = TreeNode(3, node4, node3)
'''
node3 = TreeNode(3)
node2 = TreeNode(2, None, node3)
node1 = TreeNode(1, None, node2)

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


def isBalanced(root):
    """
    对于二叉树每一层的左右节点，分别求最大深度，方法和104一样，
    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1，
    """
    que = [root]

    while que:
        curr_node = que.pop()

        if curr_node.left:
            left_depth = maxDepth(curr_node.left)
            que.append(curr_node.left)
        else:
            left_depth = 0
        if curr_node.right:
            right_depth = maxDepth(curr_node.right)
            que.append(curr_node.right)
        else:
            right_depth = 0
        if abs(left_depth - right_depth) > 1:
            return False
    return True


print(isBalanced(node1))
