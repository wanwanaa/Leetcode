# 26.删除排序数组中的重复项
# 当该数和前一个相等时不放入数组中
def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0
    c = nums[0]
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != c:
            nums[j] = nums[i]
            j += 1
            c = nums[i]
    return j