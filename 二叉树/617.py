class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# define two binary trees to be combined(with root1 and root2 respectively)
node3 = TreeNode(5)
node2 = TreeNode(2)
node1 = TreeNode(3, node3)
root1 = TreeNode(1, node1, node2)

node7 = TreeNode(7)
node6 = TreeNode(4)
node5 = TreeNode(3, None, node7)
node4 = TreeNode(1, None, node6)
root2 = TreeNode(2, node4, node5)


def mergeTrees1(root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: TreeNode
    法一: 迭代方法，用基于层序遍历的方法
    """
    if root1 == None:
        return root2
    if root2 == None:
        return root1

    que = [root1, root2]
    while que:
        size = int(len(que) / 2)
        for i in range(size):
            node1 = que.pop(0)
            node2 = que.pop(0)
            node1.val = node1.val + node2.val
            if node1.left and node2.left:
                que.extend([node1.left, node2.left])
            elif node1.left == None:
                node1.left = node2.left
            if node1.right and node2.right:
                que.extend([node1.right, node2.right])
            elif node1.right == None:
                node1.right = node2.right
    return root1


def mergeTrees2(root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: TreeNode
    法二: 递归方法
    前序遍历: 对于每一个节点，遍历顺序为 中，左，右
    """
    if root1 == None:
        return root2
    if root2 == None:
        return root1

    root1.val = root1.val + root2.val

    root1.left = mergeTrees2(root1.left, root2.left)
    root1.right = mergeTrees2(root1.right, root2.right)

    return root1


def test_function(root):
    if root == None:
        return []
    from collections import deque
    que = deque([root])
    results = []
    while que:  # 每次循环对应二叉树的每一层
        size = len(que)
        result = []
        for i in range(size):  # 遍历该层的每一个节点
            cur = que.popleft()  # 从队列的左侧出一个元素
            result.append(cur.val)
            if cur.left:  # 添加当前节点位于下一层的左节点
                que.append(cur.left)
            if cur.right:  # 添加当前节点位于下一层的右节点
                que.append(cur.right)
        results.append(result)
    return results


mergeTrees1(root1, root2)
print(test_function(root1))

