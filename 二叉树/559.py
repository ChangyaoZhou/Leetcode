class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

node6 = Node(6)
node5 = Node(5)
node4 = Node(4)
node2 = Node(2)
node3 = Node(3, [node5, node6])
node1 = Node(1, [node2, node3, node4])

def maxDepth(root):
    '''
    【法一: 层序遍历 迭代】
    if root == None:
        return 0
    que = [root]
    max_depth = 0
    while que:
        size = len(que)
        max_depth += 1
        for i in range(size):
            cur = que.pop(0)
            if cur.children:
                que.extend(cur.children)
    return max_depth
    【法二：递归】
    '''
    if root == None:
        return 0
    if not root.children:
        return 1
    max_depth = 0
    for i in range(len(root.children)):
        max_depth = max(max_depth, maxDepth(root.children[i]))
    return max_depth + 1


print(maxDepth(node1))


