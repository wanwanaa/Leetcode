# 206.反转链表
# 原地逆向
def reverseList(self, head: ListNode) -> ListNode:
    p = head
    pre = None
    while p:
        pre, p.next, p = p, pre, p.next
    return pre