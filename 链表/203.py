class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# initialize a linked list

node7 = ListNode(6)
node6 = ListNode(5, node7)
node5 = ListNode(4, node6)
node4 = ListNode(3, node5)
node3 = ListNode(6, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

'''
node1 = ListNode(7)
node2 = ListNode(7, node1)
node3 = ListNode(7, node2)
'''

def removeElements(head, val):
    # 在实际的头节点前面设置一个虚拟头节点, 这样原链表的所有节点就都可以按照统一的方式进行移除了。
    dummy_head = ListNode(0, next=head)
    cur = dummy_head
    while cur and cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next  # 删除中间的节点
            # cur = head.next
        else:
            cur = cur.next
    return dummy_head.next


def print_linked_list_val(head):
    val_list = []
    while head:
        val_list.append(head.val)
        head = head.next
    return val_list


print(print_linked_list_val(node1))
head_new = removeElements(node1, 6)
print(print_linked_list_val(head_new))
    # 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。