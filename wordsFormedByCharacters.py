class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        possible = True
        total_length = 0

        chars_dict = Counter(chars)

        print(chars_dict)

        for i in range(len(words)):
            word = words[i]
            word_dict = Counter(word)

            for key in word_dict:

                value = word_dict[key]
                if key in chars_dict:
                    
                    if value > chars_dict[key]:
                        possible = False
                        break
                else:
                    possible = False
                    break
                    

            if possible:
                total_length += len(word)
        print(word_dict)


        return total_length 

