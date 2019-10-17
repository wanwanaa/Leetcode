# 217.存在重复元素
# Python中Set属性，自动去重
def containsDuplicate(self, nums: List[int]) -> bool:
    if len(nums) != len(set(nums)) and len(nums) != 0:
        return True
    else:
        return False