class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        interval = range(left, right+1)
        flag = True

        for i in range(len(interval)):
            itr = 0
            while itr < len(ranges):
                if interval[i] not in range(ranges[itr][0],ranges[itr][-1] + 1):
                    flag = False
                else:
                    flag = True
                    break
                itr += 1
            if flag == False:
                return flag
            
        return flag
