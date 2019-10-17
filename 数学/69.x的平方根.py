# 69.x的平方根(二分法)
def mySqrt(self, x: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        return 1
    i = 1
    j = x // 2
    mid = (i+j) // 2
    while j - i > 1:
        if x > mid**2:
            i = mid
        else:
            j = mid
        mid = (i+j) //2
    if j**2 <= x:
        return j
    return mid