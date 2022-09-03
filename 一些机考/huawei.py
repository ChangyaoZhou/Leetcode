class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_Palindrome(node):
    if node == None:
        return False
    num_list = []
    curr_node = node
    while curr_node != None:
        num_list.append(curr_node.val)
        curr_node = curr_node.next
    print(num_list)
    i = 0
    j = len(num_list) - 1
    while i < j:
        if num_list[i] == num_list[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
print(is_Palindrome(node1))
