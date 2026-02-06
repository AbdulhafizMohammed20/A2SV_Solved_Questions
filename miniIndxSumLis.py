class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        least_idx_sum = float("inf")

        result = [0]
        for i in range(len(list1)):
            for j in range(len(list2)):

                if list1[i] == list2[j]:

                    if i + j < least_idx_sum :
                        least_idx_sum = i + j
                        result.pop()
                        result.append(list1[i])
                        break
                    elif i + j == least_idx_sum :
                        result.append(list1[i])
                        break
                    else:
                        break


        return result
