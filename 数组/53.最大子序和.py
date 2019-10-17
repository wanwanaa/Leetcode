# 53.最大子序和(动态规划)
# 1.之前的最大子序列和加当前数字
# 2.当前数字
def maxSubArray(self, nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i-1])
    return max(nums)
