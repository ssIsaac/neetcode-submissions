class Solution:
    def isValid(self, s: str) -> bool:
        character = {')':'(', '}':'{', ']':'['}
        arr = []

        for temp in s:
            if temp in character:
                if arr and arr[-1] == character[temp]:
                    arr.pop()
                else: 
                    return False
            else:
                arr.append(temp)
        
        return True if not arr else False