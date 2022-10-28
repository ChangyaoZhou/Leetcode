class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# initial a binary tree
node7 = TreeNode(3)
node6 = TreeNode(4)
node5 = TreeNode(4)
node4 = TreeNode(3)
node3 = TreeNode(2, node6, node7)
node2 = TreeNode(2, node4, node5)
node1 = TreeNode(1, node2, node3)


def isSymmetric(root):

    # 检查二叉树是否轴对称
    #【法一：迭代法】
    # 遍历的方式类似层序遍历，遍历从第二层开始，即root.left, root.right
    # 按外侧节点(左节点的left，右节点的right)， 内侧节点(左节点的right，右节点的left)的顺序依次进入队列
    # 每次从队列中取出两个节点(这两个节点应该是对称对应的两个节点)进行比较，
    # 如果所有左右对应的节点都相同，则true

    if root == None:
        return True
    que = [root.left, root.right]

    while que:
        left_node = que.pop(0)
        right_node = que.pop(0)
        if not left_node and not right_node:
            continue

        if not left_node or not right_node or left_node.val != right_node.val:
            return False
        que.append(left_node.left)
        que.append(right_node.right)
        que.append(left_node.right)
        que.append(right_node.left)
    return True

    # 法二：递归
    '''
    if root == None:
        return True

    def compare(node1, node2):
        # 以下是几种递归结束的条件
        if node1 and not node2:
            return False
        if node2 and not node1:
            return False
        if not node1 and not node2:  # 如果没有后续节点了，说明递归的循环结束啦
            return True
        if node1.val != node2.val:
            return False
        outside = compare(node1.left, node2.right)
        inside = compare(node1.right, node2.left)
        return outside and inside

    return compare(root.left, root.right)
    '''


print(isSymmetric(node1))




