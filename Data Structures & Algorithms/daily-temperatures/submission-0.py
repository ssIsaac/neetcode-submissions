class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []
        for i,val in enumerate(temperatures):
            
            if len(stack) == 0:
                stack.append((i, val))
            
            elif(i == len(temperatures)-1 and val < stack[-1][1]):
                while(len(stack) != 0):
                    index = stack[-1][0]
                    res[index] = 0
                    stack.pop()
                res[i] = 0
            else:
                print(stack)
                while(len(stack) != 0 and stack[-1][1] < val):
                    index = stack[-1][0]
                    res[index] = i - index
                    stack.pop()
                stack.append((i, val))
        
        return res
