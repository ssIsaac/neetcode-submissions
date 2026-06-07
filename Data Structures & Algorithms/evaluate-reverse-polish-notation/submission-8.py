class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:

            if(len(tokens) == 1):
                return int(token)

            elif token != '+' and token != '-' and token != '*' and token != '/':
                stack.append(token)

            

            else:
                res = stack[-1]
                stack.pop()
                res = int(eval(stack[-1] + token + res))
                stack.pop()
                stack.append(str(res))
                print(stack)


        return res
            
            
