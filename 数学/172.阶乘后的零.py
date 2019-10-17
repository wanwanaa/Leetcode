# 172.阶乘后的零
# 包含多少个2*5就包含多少个零
def trailingZeroes(self, n: int) -> int:
    count = 0
    while n >= 5:
        count += n // 5
        n = n// 5
    return count
