# 141.环形链表(快慢指针)
def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow = head
    fast = head
    while slow and fast:
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            return False
        if slow == fast:
            return True
    return False