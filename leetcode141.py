# problem 141
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None # ListNode.next should also be a ListNode


data = [5, 1, 7, 9]
# Define a linked list without cycle 5->1->7->9
tail1 = head1 = ListNode(data[0])
for x in data[1:]:
    tail1.next = ListNode(x) # Create and add another node
    tail1 = tail1.next # Move the tail pointer

# Define a linked list with a cycle 5->1->7->9->5->1->7->9->......
tail2 = head2 = ListNode(data[0])
for x in data[1:]:
    tail2.next = ListNode(x) # Create and add another node
    tail2 = tail2.next # Move the tail pointer
tail2.next = head2


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head == None or head.next == None:
        return False
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

# test
print(hasCycle(head1))
print(hasCycle(head2))