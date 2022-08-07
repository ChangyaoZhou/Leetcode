class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node3 = ListNode(4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

node6 = ListNode(4)
node5 = ListNode(3, node6)
node4 = ListNode(1, node5)


def mergeTwoLists(list1, list2):
    # 递归结束的条件
    if not list1:
        return list2
    if not list2:
        return list1
    # 递归
    if list1.val <= list2.val:
        # 保留list1，取mergeTwoLists(list1.next, list2)的结果(值最小的节点)作为list1.next
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        # 保留list2，取mergeTwoLists(list2.next, list1)的结果(值最小的节点)作为list2.next
        list2.next = mergeTwoLists(list2.next, list1)
        return list2


def print_linked_list_val(head):
    val_list = []
    while head:
        val_list.append(head.val)
        head = head.next
    return val_list


print(print_linked_list_val(node1))
print(print_linked_list_val(node4))
node_merge = mergeTwoLists(node1, node4)
print(print_linked_list_val(node_merge))


