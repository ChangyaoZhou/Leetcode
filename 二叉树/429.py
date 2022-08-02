class TreeNode(object):
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children


# define a N-nary tree
node6 = TreeNode(6)
node5 = TreeNode(5)
node3 = TreeNode(3, [node5, node6])
node4 = TreeNode(4)
node2 = TreeNode(2)
node1 = TreeNode(1, [node2, node3, node4])


def levelOrder(root):
    '''
    :type root: Node
    :rtype: List[List[int]]
    每个节点的子节点为children，self.children是某几个节点组成的list
    '''
    if root == None:
        return []
    from collections import deque
    que = deque([root])
    results = []
    while que:
        result = []
        size = len(que)
        for i in range(size):
            cur = que.popleft()
            result.append(cur.val)
            if cur.children:
                que.extend(cur.children)
        results.append(result)
    return results


print(levelOrder(node1))










