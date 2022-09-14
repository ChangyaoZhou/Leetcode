class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node5 = TreeNode(5)
node2 = TreeNode(2, None, node5)
node3 = TreeNode(3)
node1 = TreeNode(1, node2, node3)

#二叉树中的回溯
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


print(binary_tree_path(node1))









