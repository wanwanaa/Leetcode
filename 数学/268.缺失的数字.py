# 268.缺失的数字(位运算)
# 建立索引 a ^ b ^ b = a
def missingNumber(self, nums: List[int]) -> int:
    res = 0
    for idx, num in enumerate(nums):
        res = res ^ idx ^ num
    return res ^ len(nums)