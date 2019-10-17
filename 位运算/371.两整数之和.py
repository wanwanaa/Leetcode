# 371.两整数之和
# 溢出判断
def getSum(self, a: int, b: int) -> int:
    mask = 0x100000000
    MAX_INT = 0x7FFFFFFF
    MIN_INT = MAX_INT + 1
    while b != 0:
        temp = (a & b) << 1
        a = (a ^ b) % mask
        b = temp % mask
    return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)  