# 14.最长公共前缀
# * 依次分开
def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    res = ''
    for temp in zip(*strs):
        a = set(temp)
        print(a)
        if len(a) == 1:
            res += temp[0]
        else:
            return res
    return res