class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_arr, s2_arr = [0]*26, [0]*26
        match = 0
        l,r = 0, len(s1)-1

        for i in s1:
            s1_arr[ord(i)-97] += 1

        while(r < len(s2)):

            for i in range(l,r+1):
                s2_arr[ord(s2[i])-97] += 1
            
            for i in range(26):
                if(s1_arr[i] == s2_arr[i]):
                    match += 1
            print(l)
            print(r)
            print(match)

            if (match == 26): 
                return True
            # if(s1_arr == s2_arr):
            #     return True
            else:
                s2_arr = [0]*26
                r += 1
                l += 1
                match = 0

        return False



    