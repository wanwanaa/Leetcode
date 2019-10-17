# 66.加一
def plusOne(self, digits: List[int]) -> List[int]:
    i = len(digits) - 1
    temp = 1
    while i >= 0 and temp != 0:
        digits[i], temp = (digits[i] + temp) % 10, (digits[i] + temp) // 10
        i -= 1
    if temp != 0:
        digits.insert(0, temp)
    return digits