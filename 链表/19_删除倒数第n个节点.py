class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_nodelist(val_nums):
    head = ListNode(val_nums[0])
    curr_pos = head
    for i in range(1, len(val_nums)):
        node = ListNode(val_nums[i])
        curr_pos.next = node
        curr_pos = curr_pos.next
    return head


def print_nodelist(head):
    node_vals = []
    while(head):
        node_vals.append(head.val)
        head = head.next
    print(node_vals)

# 法一 双指针
'''
我们可以使用两个指针slow和fast同时对链表进行遍历，并且fast比slow超前n个节点。当fast遍历到链表的末尾时，slow就恰好处于倒数第n个节点。
为了防止要删除的节点正好是头节点，我们在头节点前面加一个dummy node
 
def removeNthFromEnd(head, n):
    if not head.next:
        return None
    virtual_head = ListNode(0, head)
    slow = virtual_head
    fast = virtual_head
    i = 0
    while(fast.next):
        if i >= n:
            slow = slow.next
        fast = fast.next
        i += 1
    # while 循环结束时，slow指针正好位于要删除的节点的前一个节点
    slow.next = slow.next.next
    return virtual_head.next
'''

# 法二 先计算链表长度
'''
一种容易想到的方法是，我们首先从头节点开始对链表进行一次遍历，得到链表的长度 L。
随后我们再从头节点开始对链表进行一次遍历，当遍历到第L-n+1个节点时，它就是我们需要删除的节点。
当遍历到第L-n个节点时，找到了需要删除的节点的前面一个节点，只需要修改一次指针，就能完成删除操作。
 
'''
def get_length(head):
    nodelist_len = 0
    while (head):
        nodelist_len += 1
        head = head.next
    return nodelist_len


def removeNthFromEnd(head, n):
    if not head.next:
        return None
    nodelist_len = get_length(head)
    virtual_head = ListNode(0, head)
    curr_pos = virtual_head
    for i in range(nodelist_len - n):
        curr_pos = curr_pos.next
    curr_pos.next = curr_pos.next.next
    return virtual_head.next


val_nums = [1, 2, 3, 4, 5]
head = create_nodelist(val_nums)
head = removeNthFromEnd(head, 5)
print_nodelist(head)
