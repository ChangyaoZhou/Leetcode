class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# define a binary tree 可以从上到下定义也可以从下向上定义
node3 = TreeNode(3)
node2 = TreeNode(2, node3)
node1 = TreeNode(1, None, node2) # root


def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    后序遍历: 对于每一个节点，遍历顺序为 左，右，中
    法一: 递归
    result = []

    def traversal(root):
        if root == None:
            return
        traversal(root.left)
        traversal(root.right)
        result.append(root.val)

    traversal(root)
    return result

    法二:
    先序遍历是中左右，后续遍历是左右中，那么我们只需要调整一下先序遍历的代码顺序，就变成中右左的遍历顺序，
    然后在反转result数组，输出的结果顺序就是左右中了
    e.g. 现有二叉树      5
                      / \
                    4    6
                   / \
                  1   2
    stack      action       result
    5          5出栈         5
    4，6       6出栈         5，6
    4         4出栈         5，6，4
    1，2      2出栈         5，6，4，2
    1        1出栈         5，6，4，2，1 ——翻转——> 1, 2, 4, 6, 5
    """

    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        # 中结点先处理
        result.append(node.val)
        # 左孩子先入栈
        if node.left:
            stack.append(node.left)
        # 右孩子后入栈
        if node.right:
            stack.append(node.right)
    # 将最终的数组翻转！！！
    return result[::-1]

print(postorderTraversal(node1))

