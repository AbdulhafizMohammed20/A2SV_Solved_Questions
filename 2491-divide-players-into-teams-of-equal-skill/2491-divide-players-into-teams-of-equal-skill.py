class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left = 0
        right = len(skill) - 1 
        teams = []
        
        while left < right :
            teams.append([skill[left] , skill[right]])
            left += 1
            right -= 1
        equal = sum(teams[0])
        i = 1
        while i < len(teams) :

            if sum(teams[i]) == equal:
                i += 1
            else:
                return -1
        chemistry_sum = 0
        for team in teams:
            p1,p2 = team
            chemistry_sum += p1*p2
        
        return chemistry_sum
            



