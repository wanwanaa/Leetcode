# 70.爬楼梯
# f(n)=f(n)+f(n-1)
def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    num = 0
    num_1 = 1
    num_2 = 1
    for i in range(2, n+1):
        num = num_1 + num_2
        num_1 = num_2
        num_2 = num
    return num