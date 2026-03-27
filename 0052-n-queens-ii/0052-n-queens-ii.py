class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [False] * n
        posDiag = [False] * (2 * n)
        negDiag = [False] * (2 * n)
        self.count = 0  

        def backtrack(r):
            if r == n:
                self.count += 1
                return
            
            for c in range(n):

                if cols[c] or posDiag[r + c] or negDiag[r - c + n]:
                    continue
                
                cols[c] = posDiag[r + c] = negDiag[r - c + n] = True
                
                backtrack(r + 1)
               
                cols[c] = posDiag[r + c] = negDiag[r - c + n] = False

        backtrack(0)
        return self.count
