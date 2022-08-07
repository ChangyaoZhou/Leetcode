class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# initialize a linked list
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2


def hasCycle(head):
    """
    链表的基本介绍！！！ https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E9%93%BE%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.md
    给你一个链表的头节点 head ，判断链表中是否有环。
    使用双指针，一个指针每次移动一个节点，一个指针每次移动两个节点，如果存在环，那么这两个指针一定会相遇
    If ListNode.next == None, 则说明该节点后面没有连接另一个节点。
    e.g.上述链表 (有闭环)
    num of cycle        slow.val        fast.val
    0                   3               3
    1                   2               0
    2                   0               2
    3                   2               -4
    4                   0               0    ---> true

    e.g. linked list 3->4->5->6 (没有闭环)
    num of cycle        slow.val        fast.val
    0                   3               3
    1                   4               5
    2                   5               None
    3    ----> false
    """
    if head == None or head.next == None:
        return False
    fast_pointer = head
    slow_pointer = head
    while fast_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next.next
        if fast_pointer == slow_pointer:
            return True
    return False


print(hasCycle(node1))





