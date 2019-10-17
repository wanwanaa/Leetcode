# 169.求众数(摩尔投票法)
# 相等加1，不等减1，抵消完后换数字
def majorityElement(self, nums):
    count = 0
    now = None    
    for i in nums:
        if count == 0:
            now = i     
        count += 1 if now == i else -1 
    return now 