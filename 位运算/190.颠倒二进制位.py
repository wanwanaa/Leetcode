# 190.颠倒二进制位
# 循环右移末位+1（左移符号位溢出）
def reverseBits(self, n):
    res = 0
    for i in range(32):
        res = res << 1
        res += n & 1
        n = n >> 1
    return res