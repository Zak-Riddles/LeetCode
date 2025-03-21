// Last updated: 3/20/2025, 10:51:19 PM
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        table = {}
        for row in range(numRows):
            table[row] = []
        row = -1
        is_down = True

        for char in s:
            if (row <= 0):
                is_down = True
            elif (row == numRows - 1):
                is_down = False
            
            if is_down:
                row += 1
                table[row].append(char)
            else:
                row -= 1
                table[row].append(char)
        
        result = []
        for row_num in range(numRows):
            result.append("".join(table[row_num]))
        
        return "".join(result)