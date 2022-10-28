class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node5 = TreeNode(5)
node2 = TreeNode(2, None, node5)
node3 = TreeNode(3)
node1 = TreeNode(1, node2, node3)

#二叉树中的回溯，【深度优先搜索】
def binary_tree_path(root):
    result = []
    path = []
    if root == None:
        return result

    def backtracking(node):
        path.append(node.val)
        #回溯结束的条件：当前节点没有后续的左节点或右节点
        if node.left == None and node.right == None:
            path_str = ''
            for num in path:
                path_str = path_str + str(num) + '->'
            result.append(path_str[:-2])
            return

        if node.left != None:
            backtracking(node.left)
            path.pop()
        if node.right != None:
            backtracking(node.right)
            path.pop()

    backtracking(root)
    return result

"""
用迭代的方法求二叉树的所有路径，即【广度优先搜索】，que中的每一项是一个tuple，(node, 从root走到当前节点处的path)
"""
def binary_tree_path2(root):
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
            # 当当前节点是叶子节点时，将当前路径存下来
            if not curr_node.left and not curr_node.right:
                path_str = ''
                for num in path:
                    path_str = path_str + str(num) + '->'
                result.append(path_str[:-2])
    return result


print(binary_tree_path(node1))
print(binary_tree_path2(node1))









