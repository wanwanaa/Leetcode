# 13.罗马数字转整数
# 建立对应索引，注意判断加减条件
def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    num = 0
    for i in range(len(s)):
        if i<len(s)-1 and dic[s[i+1]] > dic[s[i]]:
            num -= dic[s[i]]
        else:
            num += dic[s[i]]
    return num