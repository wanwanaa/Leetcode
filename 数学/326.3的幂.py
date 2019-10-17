# 326.3的幂
def isPowerOfThree(self, n: int) -> bool:
    if n <= 0:
        return False
    if n == 1:
        return True
    while n > 3:
        if n % 3 == 0:
            n = n//3
        else:
            return False
    if n % 3 == 0:
        return True