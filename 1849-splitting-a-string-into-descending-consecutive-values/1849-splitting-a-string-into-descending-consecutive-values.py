class Solution:
    def splitString(self, s: str) -> bool:
        
        def f(arr, s):
            # print(arr)
            for i in range(1, len(arr)):
                if arr[i] != arr[i-1] - 1:
                    return False
            if not s and len(arr) > 1:
                return True
            result = False
            for i in range(len(s)):
                arr.append(int(s[:i+1]))
                result = result or f(arr, s[i+1:])
                arr.pop()
            return result
        return f([], s)