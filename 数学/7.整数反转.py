# 7.整数反转
# 负数取模下取整
def reverse(self, x: int) -> int:
    while x != 0:
        pop = x % 10
        if (temp > sys.maxsize/10) or (temp == sys.maxsize/10 and pop > 7):
            return 0
        if (temp < (-sys.maxsize-1)/10 0r (temp == (-sys.maxsize-1)/10 and pop < -8):
            return 0
        temp = temp * 10 + pop
        x = x // 10
    return temp