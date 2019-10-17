# 160.相交链表(找到单链表的起始节点)
# 1.将两个链表拼接 A+B和B+A
# 2.从头开始找，当相等时即为拼接节点
def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    pa = headA
    pb = headB
    while pa != pb:
        pa = pa.next if pa else headB
        pb = pb.next if pb else headA
    return pa