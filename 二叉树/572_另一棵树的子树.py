class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node1 = TreeNode(1)
node2 = TreeNode(2)
node4 = TreeNode(4, node1, node2)
node5 = TreeNode(5)
node3 = TreeNode(3, node4, node5)

subnode1 = TreeNode(1)
subnode2 = TreeNode(2)
subnode4 = TreeNode(4, subnode1, subnode2)


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


def isSubtree(root, subRoot):
    #先用层序遍历寻找和subroot数值相同的节点，再判断该节点和subroot是否为相同的树，同100题
    if not root and not subRoot:
        return True
    que = [root]
    while que:
        size = len(que)
        for _ in range(size):
            curr_node = que.pop(0)
            if curr_node.val == subRoot.val and isSameTree(curr_node, subRoot):
                return True
            if curr_node.left:
                que.append(curr_node.left)
            if curr_node.right:
                que.append(curr_node.right)
    return False


print(isSubtree(node3, subnode4))


