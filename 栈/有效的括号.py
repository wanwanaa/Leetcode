# 20.有效的括号（左右括号的匹配）
# 1.初始化：a.右左括号建立字典匹配 
#           b.新建一个栈用来匹配括号
# 2.判断： a.左括号->入栈
#          b.右括号进行匹配，匹配成功栈顶元素出栈，失败返回False
# 3.最终栈为空返回True
def isValid(self, s: str) -> bool:
        if not s:
            return True
        temp = []
        dic = {')':'(', ']':'[', '}':'{'}
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                temp.append(s[i])
            else:
                if temp and dic[s[i]] == temp[-1]:
                    temp.pop()
                else:
                    return False
        if temp:
            return False
        else:
            return True