class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
        
        rows_n_1 = self.generate(numRows-1)
        
        row_n = [1]
        for i in range(1, len(rows_n_1[-1])):
            row_n.append(rows_n_1[-1][i]+rows_n_1[-1][i-1])
        
        row_n.append(1)
        rows_n_1.append(row_n)
        
        return rows_n_1
        
        
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        triangle = []
        
        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1
            
            for j in range(1, len(row)-1):
                row[j] = triangle[-1][j-1] + triangle[-1][j]
            
            triangle.append(row)
        
        return triangle 
