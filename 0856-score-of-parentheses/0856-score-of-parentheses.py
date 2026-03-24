class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = [] 
     
        for ch in s:

            if ch == '(' :
                stack.append(0)
            
            else :
                if stack[-1] == 0 :
                    stack.pop()
                    stack.append(1)
                else:
                    total = 0

                    while stack[-1] != 0 :
                        total += stack.pop()
                    
                    stack.pop()
                    stack.append(2 * total)
                    
        return sum(stack)