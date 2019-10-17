# 283.移动零(双指针)
# 不为0的数放入数组，最后在数组末尾填0
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] == 0:
            j += 1
        else:
            nums[i] = nums[j]
            i += 1
            j += 1
    while i < len(nums):
        nums[i] = 0
        i += 1
    return nums