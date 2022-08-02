class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# define a binary tree
node4 = TreeNode(4)
node5 = TreeNode(5)
node3 = TreeNode(3, None, node4)
node2 = TreeNode(2, None, node5)
node1 = TreeNode(1, node2, node3)



def rightSideView(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    注意: 不能只考虑右节点，当二叉树中每个节点都只有左节点时，该二叉树也有右视图
    """
    if root == None:
        return []
    from collections import deque
    que = deque([root])
    result = []
    while que:
        result.append(que[-1].val)  # 对于每一层的数字，只取最后一项(最右侧的一个节点)
        size = len(que)
        for _ in range(size):
            cur = que.popleft()
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
    return result

print(rightSideView(node1))
