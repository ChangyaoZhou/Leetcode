class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node6 = TreeNode(6)
node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(6, node6)
node2 = TreeNode(2, node4, node5)
node1 = TreeNode(1, node2, node3)


def countNodes(root):
    """
    层序遍历 迭代
    if not root:
        return 0

    from collections import deque
    que = deque([root])
    count = 0
    while que:
        size = len(que)
        count += size
        for i in range(size):
            curr_node = que.pop()
            if curr_node.left:
                que.append(curr_node.left)
            if curr_node.right:
                que.append(curr_node.right)
    return count
    """
    if not root:
        return 0
    if not root.right and not root.left:
        return 1
    left_num = countNodes(root.left)
    right_num = countNodes(root.right)
    return left_num + right_num + 1


print(countNodes(node1))
