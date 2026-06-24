class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = defaultdict(int)
        l,r = 0,1
        maxVal = 0
        if(len(s) <= 1):
            return len(s)
        
        tmp[s[l]] = l

        while(r < len(s)):
            
            # if(s[r] not in tmp):
            #     print(tmp)
            #     print(r,s[r], r-l+1)
            #     tmp[s[r]] = r
            #     maxVal = max(maxVal, r-l+1)
            #     r += 1
            # else:
            #     val = tmp.pop(s[r])
            #     l += 1
            #     tmp[s[l]] = l


            if(s[r] in tmp): ## if char exists in dict
                val = tmp.pop(s[r])
                l = val + 1
                for k in list(tmp.keys()):
                    if tmp[k] < l:
                        del tmp[k]
                print(tmp)
                

            else:
                tmp[s[r]] = r
                maxVal = max(maxVal, len(tmp))
                r += 1

        
            

                
            
            

            
        
        return maxVal