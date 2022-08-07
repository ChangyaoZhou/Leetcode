class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# initialize a linked list
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

def print_linked_list_val(head):
    val_list = []
    while head:
        val_list.append(head.val)
        head = head.next
    return val_list

def reverseList(head):
    if head == None:
        return
    pre = None
    cur = head
    while cur:
        # 对于cur, pre等每个值来说，都是先把他赋给别的值，然后再给自己赋值
        cache = cur.next  # 先将cur.next缓存下来
        cur.next = pre
        pre = cur
        cur = cache
    # 当cur为none时结束循环，此时的pre是反转后链表的头节点
    return pre


