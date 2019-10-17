# 242.有效的字母异位词(两个单词是否包含同样的数字)
def isAnagram(self, s: str, t: str) -> bool:
    if len(t) != len(s):
        return False
    t = list(t)
    for c in s:
        if c in t:
            t.remove(c)
        else:
            return False
    return True
