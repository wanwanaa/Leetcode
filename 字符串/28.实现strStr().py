# 28.实现strStr()
# KMP
def strStr(self, haystack: str, needle: str) -> int:
    def get_next(needle):
        next_ = [-1]*len(needle)
        i = 0 
        j = -1
        while(i < len(next_)-1):
            if j == -1 or needle[i] == needle[j]:
                j += 1
                i += 1
                next_[i] = j
            else:
                j = next_[j]
        return next_
    
    
    if not needle:
        return 0
    next_ = get_next(needle)
    i = 0
    j = 0
    while(i < len(haystack) and j < len(needle)):
        if j == -1 or haystack[i] == needle[j]:
            j += 1
            i += 1
        else:
            j = next_[j]
    if j == len(needle):
        return i-j
    else:
        return -1