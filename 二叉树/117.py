class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# define a binary tree
node7 = Node(7)
node5 = Node(5)
node4 = Node(4)
node3 = Node(3, None, node7)
node2 = Node(2, node4, node5)
node1 = Node(1, node2, node3)


def connect(root):
    """
    :type root: Node
    :rtype: Node
    本题中的二叉树不一定是完美二叉树
    """
    if root == None:
        return None
    #from collections import deque 也可以不用deque，用list.pop(0)就可以实现popleft()
    que = [root]
    #que = deque([root])
    next_result = []
    while que:
        size = len(que)
        for i in range(size):
            cur = que.pop(0)
            #cur = que.popleft()
            next_result.append(cur.val)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
            if i < size - 1:
                cur.next = que[0]
            # i=size-1时，que中所有当前层的节点已经全部被删除了，直接break，最右侧的节点的next指针是None(初始化就是None，不用改)

    return root



# test function
# 输入二叉树的root node,返回改二叉树的层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
def test(root):
    if root == None:
        return []
    output = []
    from collections import deque
    que = deque([root])
    while que:
        output.append(que[0].val)
        size = len(que)
        for i in range(size):
            cur = que.popleft()
            if cur.next:
                output.append(cur.next.val)
            else:
                output.append('#')
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
    return output


# test connect function
root_node = connect(node1)
print(test(root_node))