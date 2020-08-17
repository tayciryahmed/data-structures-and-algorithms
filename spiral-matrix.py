class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 0 : return []
        
        max_row, max_col  = len(matrix)-1, len(matrix[0])-1
        min_row, min_col = 0, 0
        
        ans = [] 
        
        while min_row <= max_row and min_col <= max_col:
            
            for i in range(min_col, max_col+1):
                ans.append(matrix[min_row][i])
            
            min_row += 1
            
            for i in range(min_row, max_row+1):
                ans.append(matrix[i][max_col])
            
            max_col -= 1
            
            if min_row <= max_row:
            
                for i in range(max_col, min_col-1, -1):
                    ans.append(matrix[max_row][i])
            
            max_row -= 1
            
            if min_col <= max_col:
            
                for i in range(max_row, min_row-1, -1):
                    ans.append(matrix[i][min_col])
            
            min_col += 1
        
        return ans 
        
