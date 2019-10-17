# 204.计算质数(筛法)
# 按顺序从第一个数开始一次去掉后面该数的倍数
def countPrimes(self, n: int) -> int:
    if n < 3:
        return 0
    count = [1] * n 
    count[0] = 0
    count[1] = 0
    for i in range(2, int(n**0.5)+1):
        for j in range(i, n, i):
            if j != i:
                count[j] = 0
    return sum(count)