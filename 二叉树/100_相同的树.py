class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node3q = TreeNode(3)
node2q = TreeNode(2)
node1q = TreeNode(1, node2q, node3q)

node3p = TreeNode(3)
node2p = TreeNode(2)
node1p = TreeNode(1, node2p, node3p)


def isSameTree(p, q) -> bool:
    if not p and not q:
        return True
    elif not p and q:
        return False
    elif p and not q:
        return False

    if p.val != q.val:
        return False

    is_same_left = isSameTree(p.left, q.left)
    is_same_right = isSameTree(p.right, q.right)
    return is_same_left and is_same_right


print(isSameTree(node1p, node1q))
