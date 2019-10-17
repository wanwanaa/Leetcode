# 234.回文链表(快慢指针)
# 当快指针到尾部时，慢指针刚好在中间
def isPalindrome(self, head: ListNode) -> bool:
    nums = []
    p = head
    while p:
        nums.append(p.val)
        p = p.next
    for i in range(len(nums)//2):
        if nums[i] != nums[len(nums)-1-i]:
            return False
    return True