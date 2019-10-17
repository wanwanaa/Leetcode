# 1.两数之和
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = dict()
    for i, num in enumerate(nums):
        temp = target - num
        if dic.get(temp) is not None:
            return [dic[temp], i]
        else:
            dic[num] = i
    return None