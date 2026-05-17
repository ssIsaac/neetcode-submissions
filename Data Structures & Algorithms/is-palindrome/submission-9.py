class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for tmp in s:
            if(tmp.isalnum()):
                newS += tmp.lower()
            continue

        
        return newS == newS[::-1] 