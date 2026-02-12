class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict_word1 = Counter(word1)
        dict_word2 = Counter(word2)

        
        if set(dict_word1.keys()) != set(dict_word2.keys()):
            return False

       
        if sorted(dict_word1.values()) != sorted(dict_word2.values()):
            return False

        return True
