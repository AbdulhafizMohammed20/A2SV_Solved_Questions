class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()

        res = []
        i = len(piles) -1

        while len(res) < len(piles) // 3:
            i -= 1

            res.append(piles[i])

            i -= 1

        return sum(res)



        