class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:



        ransomNote_dict = Counter(ransomNote)
        magazine_dict = Counter(magazine)

        for key  in ransomNote_dict:
            if   ransomNote_dict[key] > magazine_dict[key]:
                return False

        
        return True