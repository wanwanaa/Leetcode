# 198.打家劫舍(不能连续偷)
# 1.前一家没有偷
# 2.偷了前一家
def rob(self, nums: List[int]) -> int:
    last = 0
    now = 0
    for i in range(len(nums)):
        temp = now
        now = max(last+nums[i], now)
        last = temp
    return now