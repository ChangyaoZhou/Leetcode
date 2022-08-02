class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# define a binary tree 可以从上到下定义也可以从下向上定义
node3 = TreeNode(3)
node2 = TreeNode(2, node3)
node1 = TreeNode(1, None, node2) # root


def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    前序遍历: 对于每一个节点，遍历顺序为 中，左，右
    法一: 递归
    result = []

    def traversal(root):  # 在preorderTraversal函数里面定义traversal函数，可以直接调用result，不用把他加入traversal的参数
        if root == None:
            return # 无事发生
        result.append(root.val)
        traversal(root.left)
        traversal(root.right)

    traversal(root)
    return result

    法二: 前序遍历是中左右，每次先处理的是中间节点，那么先将根节点放入栈中，然后将右孩子加入栈，再加入左孩子。
        为什么要先加入 右孩子，再加入左孩子呢？ 因为这样出栈的时候才是中左右的顺序。
    e.g. 现有二叉树      5
                      / \
                    4    6
                   / \
                  1   2
    stack      action       result
    5          5出栈         5
    6，4       4出栈         5，4
    6，2，1    1出栈         5，4，1
    6，2      2出栈         5，4，1，2
    6        6出栈         5，4，1，2，6
    """
    if root == None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val) # 先存下来中节点
        if node.right:
            stack.append(node.right) # 右子节点先入栈
        if node.left:
            stack.append(node.left) # 左子节点后入栈
    return result





# test code
print(preorderTraversal(node1))




