class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        res = []

        for size in range(len(arr) , 0, -1):
            max_indx = arr.index(max(arr[:size]))

            arr[:max_indx+1] = reversed(arr[:max_indx + 1])
          
            res.append(max_indx + 1)
            arr[:size] = reversed(arr[:size])
            
            res.append(size)
        return res