# 189.旋转数组
# 原地反转->前k个反转->后k个反转
# 注：对k取余
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse_nums(nums, i, j):
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    k %= len(nums)
    reverse_nums(nums, 0, len(nums)-1)
    reverse_nums(nums, 0, k-1)
    reverse_nums(nums, k, len(nums)-1)
    return nums