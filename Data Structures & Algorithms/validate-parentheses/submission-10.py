class Solution:
    def isValid(self, s: str) -> bool:
        character = {')':'(', '}':'{', ']':'['}
        arr = []

        if(s[0] != '{' and s[0] != '(' and s[0] !='['):
            return False

        for temp in s:
            if(temp == '{' or temp == '(' or temp == '['):
                arr.append(temp)
            else:
                if(len(arr) == 0 or character[temp] != arr[-1]):
                    return False
                arr.pop()
            print("hello")
        
        if not arr:
            return True
        return False