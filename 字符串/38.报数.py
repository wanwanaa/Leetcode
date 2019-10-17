# 报数
# 1，11, 21, 1211, 111221
def countAndSay(self, n: int) -> str:
    s = '1'
    for i in range(1, n):
        s = list(s)
        s_next = ''
        c = s[0]
        count = 1
        for j in range(1, len(s)):
            if j+1 == len(s):
                if s[j] == c:
                    count += 1
                else:
                    s_next = s_next + str(count) + c
                    count = 1
                    c = s[j]
            elif s[j] == c:
                count += 1
            else:
                s_next = s_next + str(count) + c
                count = 1
                c = s[j]
        s_next = s_next + str(count) + c
        s = copy.deepcopy(s_next)
    return s