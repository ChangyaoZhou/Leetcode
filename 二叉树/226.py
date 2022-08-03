class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node7 = TreeNode(9)
node6 = TreeNode(6)
node5 = TreeNode(3)
node4 = TreeNode(1)
node3 = TreeNode(7, node6, node7)
node2 = TreeNode(2, node4, node5)
node1 = TreeNode(4, node2, node3)


def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    法一: 层序遍历，迭代，简单易懂！！
    if root == None:
        return None
    que = [root]
    while que:
        size = len(que)
        for i in range(size):
            cur = que.pop(0)
            if cur.left and cur.right:
                tmp_node = cur.left
                cur.left = cur.right
                cur.right = tmp_node
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
    return root
    法二: 递归
    """
    if root == None:
        return None
    tmp_node = root.left
    root.left = root.right
    root.right = tmp_node
    root.left = invertTree(root.left)
    root.right = invertTree(root.right)
    return root


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


root = invertTree(node1)
print(test_function(root))

