class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# define a binary tree 可以从上到下定义也可以从下向上定义
node3 = TreeNode(3)
node2 = TreeNode(2, node3)
node1 = TreeNode(1, None, node2) # root


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    中序遍历: 对于每一个节点，遍历顺序为 左，中，右
    法一: 递归
    result = []

    def traversal(root):
        if root == None:
            return
        traversal(root.left)
        result.append(root.val)
        traversal(root.right)

    traversal(root)
    return result

    法二:
    前序遍历中，因为前序遍历的顺序是中左右，先访问的元素是中间节点，要处理的元素也是中间节点，
    所以刚刚才能写出相对简洁的代码，因为要访问的元素和要处理的元素顺序是一致的，都是中间节点。
    但是对于中序遍历，问题在于【处理顺序和访问顺序是不一致的】
    那么在使用迭代法写中序遍历，就需要借用指针的遍历来帮助访问节点，栈则用来处理节点上的元素
    e.g. 现有二叉树      5
                      / \
                    4    6
                   / \
                  1   2
    stack    cur    action       result
    []        5      5入栈         []
    5         4      4入栈         []
    5,4       1      1入栈         []
    5,4,1  None->1    pop         [1]
    5      None->4    pop         [1,4]
    5         2      2入栈         [1,4]
    5      None->2    pop         [1,4,2]
    []     None->5    pop         [1,4,2,5]
    []        6      6入栈         [1,4,2,5]
    6      None->6    pop         [1,4,2,5,6]
    """
    stack = []
    result = []
    if root == None:
        return []
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
    return result


print(inorderTraversal(node1))


