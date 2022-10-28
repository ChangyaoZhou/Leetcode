class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node5 = TreeNode(5)
node4 = TreeNode(4)
node7 = TreeNode(7)
node6 = TreeNode(6, left=node7)
node3 = TreeNode(3, right=node5)
node2 = TreeNode(2, left=node4, right=node6)
node1 = TreeNode(1, left=node2, right=node3)


def leaf_path(root):
    if not root:
        return []
    result = []
    path = []

    def backtracking(root):
        path.append(root.val)
        if not root.left and not root.right:
            result.append(path[:])
            return

        # path.append(root.val)
        if root.left:
            backtracking(root.left)
            path.pop()
        if root.right:
            backtracking(root.right)
            path.pop()

    backtracking(root)
    return result


def leaf_path2(root):
    result = []
    que = [(root, [root.val])]
    while que:
        size = len(que)
        for _ in range(size):
            curr_node, path = que.pop(0)
            if curr_node.left:
                que.append((curr_node.left, path + [curr_node.left.val]))
            if curr_node.right:
                que.append((curr_node.right, path + [curr_node.right.val]))
            if not curr_node.left and not curr_node.right:
                result.append(path)
    return result


print(leaf_path(node1))
print(leaf_path2(node1))

