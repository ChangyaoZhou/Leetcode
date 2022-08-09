class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node5 = ListNode(3)
node4 = ListNode(3, node5)
node3 = ListNode(2, node4)
node2 = ListNode(1, node3)
node1 = ListNode(1, node2)


def deleteDuplicates(head):
    """
    e.g. linked list 1->1->2->3->3
    head 1(1)  head.next = deleteDuplicates(head.next)
            head 1(2)  head.next = deleteDuplicates(head.next)
                    head 2  head.next = deleteDuplicates(head.next)
                            head 3(1)  head.next = deleteDuplicates(head.next)
                                    head 3(2)  head.next = deleteDuplicates(head.next)
                                            head None  向上一层return None
                                    head 3(2)  head.next = None 向上一层返回head 3(2)
                            head3(1) head.next = head 3(1)  head.val == head.next.val  ->向上一层返回head 3(2)
                    head 2  head.next = head 3(2)  向上一层返回head 2
            head1(2)  head.next = head2  向上一层返回head 1(2)
    head 1(1) head.next = head 1(2)  head.val == head.next.val  ->向上一层返回head 1(2)
    return head1(2)

    """
    # 如果链表为空
    if head == None:
        return head
    # 如果链表只有一项
    if head.next == None:
        return head
    head.next = deleteDuplicates(head.next)
    if head.val == head.next.val:
        return head.next
    else:
        return head


def print_linked_list_val(head):
    val_list = []
    while head:
        val_list.append(head.val)
        head = head.next
    return val_list


print(print_linked_list_val(node1))
head_new = deleteDuplicates(node1)
print(print_linked_list_val(head_new))
