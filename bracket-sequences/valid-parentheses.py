class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True 
        
        if len(s) % 2 != 0:
            return False

        map = {"}":"{", ")":"(", "]":"["}
        arr = []

        for c in s:
            if c == "{" or c == "(" or c == "[":
                arr.append(c)
            else:
                if len(arr) == 0:
                    return False
                
                top = arr.pop()
                if map[c] != top:
                    return False
        
        return len(arr) == 0