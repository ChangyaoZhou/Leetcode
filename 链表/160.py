class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

# initialize a linked list
node6 = ListNode(4)
node5 = ListNode(2, node6)
node4 = ListNode(3, node5)
node3 = ListNode(1, node5)
node2 = ListNode(9, node3)
node1 = ListNode(1, node2)

def getIntersectionNode(headA, headB):
    """
    当访问 A 链表的指针访问到链表尾部时，令它从链表 B 的头部开始访问链表 B；
    同样地，当访问 B 链表的指针访问到链表尾部时，令它从链表 A 的头部开始访问链表 A。
    这样就能控制访问 A 和 B 两个链表的指针能同时访问到交点。
    e.g.  1-->9-->1-->2-->4
                  3-->2-->4   交点在2
    step    1          2   3   4    5         6       7         8
    h1      1(headA)   9   1   2    4         none    3(headB)  2
    h2      3          2   4   none 1(headA)  9       1         2   ---> intersection at 2
    """

    h1 = headA
    h2 = headB
    while h1 != h2:
        # 若h1为None，则代表h1走到了尾部，接上headB
        if not h1:
            h1 = headB
        else:
            h1 = h1.next
        # 若h2为None，则代表h2走到了尾部，接上headA
        if not h2:
            h2 = headA
        else:
            h2 = h2.next
        # 若h1，h2都走完了两个链表，还是没有相交，则说明没有交点
        if h1 == None and h2 == None:
            return h1
    return h1


print(getIntersectionNode(node1, node4).val)
