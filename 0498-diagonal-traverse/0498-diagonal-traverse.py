class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        result = []

        dir = 1
        row, col = 0, 0
        while len(result) < rows*cols:
            if(dir == 1):
                result.append(mat[row][col])
                row -= 1
                col += 1
                if(not inbound(row, col)):
                    row += 1
                    col -= 1
                    if(inbound(row, col+1)):
                        col += 1
                    elif(inbound(row+1, col)):
                        row += 1
                    dir = 0
            else:
                result.append(mat[row][col])
                row += 1
                col -= 1
                if(not inbound(row, col)):
                    row -= 1
                    col += 1
                    if(inbound(row+1, col)):
                        row += 1
                    elif(inbound(row, col+1)):
                        col += 1
                    dir = 1
        return result

        