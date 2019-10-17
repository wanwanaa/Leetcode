# 21.合并两个有序链表
# 注：新建一个头结点用来添加结果
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode(-1)
    pre = result
    while l1 and l2:
        if l1.val <= l2.val:
            pre.next = l1
            l1 = l1.next
        else:
            pre.next = l2
            l2 = l2.next
        pre = pre.next
    if l2:
        pre.next = l2
    if l1:
        pre.next = l1
    return result.next