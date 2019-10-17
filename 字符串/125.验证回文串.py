# 125.验证回文串
# 判断时去掉非字母数字字符
def isPalindrome(self, s: str) -> bool:
    if not s:
        return True
    s = s.lower()
    s = s.replace(' ', '')
    i = 0
    j = len(s)-1
    while i < j:
        if (s[i] > 'z' or s[i] < 'a') and (s[i] > '9' or s[i] < '0'):
            i += 1
        elif (s[j] > 'z' or s[j] < 'a') and (s[j] > '9' or s[j] < '0'):
            j -= 1
        elif s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True