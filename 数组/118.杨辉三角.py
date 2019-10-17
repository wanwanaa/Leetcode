# 118.杨辉三角
def generate(self, numRows: int) -> List[List[int]]:
    result = []
    for i in range(0, numRows):
        row = [1]*(i+1)
        for j in range(1, i):
            row[j] = result[i-1][j-1] + result[i-1][j]
        result.append(row)
    return result