# 387.字符串中的第一个唯一字符(哈希)
# 建立字典统计字符串中没个字母的个数
# 按字符串顺序遍历，输出第一个值为1的索引值
def firstUniqChar(self, s: str) -> int:
    s = list(s)
    dic = dict()
    for c in s:
        if not dic.get(c):
            dic[c] = 1
        else:
            dic[c] += 1 
    for i in range(len(s)):
        if dic[s[i]] == 1:
            return i
    return -1