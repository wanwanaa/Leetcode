# 202.快乐数(双指针)
# 快慢指针的数是否会相同
def isHappy(self, n: int) -> bool:
    def square(num):
        result = 0
        while num > 0:
            result = result + (num%10)**2
            num = num // 10
        return result
    slow = n
    fast = n
    while(True):
        slow = square(slow)
        fast = square(fast)
        fast = square(fast)
        if slow == fast:
            break
    if slow == 1:
        return True
    else:
        return False
