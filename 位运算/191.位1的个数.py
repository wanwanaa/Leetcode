# 191.位1的个数
# n&1右移
def hammingWeight(self, n):
    count = 0
        while n:
            count += n&1
            n >>= 1
        return count