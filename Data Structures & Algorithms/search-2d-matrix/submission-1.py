class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        

        while(l <= r):
            mid = (l+r)//2
            curr = matrix[mid]
            
            if(curr[0] > target):
                r = mid - 1
            elif (curr[len(curr)-1] < target):
                l = mid + 1
            else:
                l_inner,r_inner = 0, len(curr)-1
                while(l_inner <= r_inner):
                    mid_inner = (l_inner + r_inner)//2
                    if(curr[mid_inner] > target):
                        r_inner = mid_inner - 1
                    elif (curr[mid_inner] == target):
                        return True
                    else:
                        l_inner = mid_inner + 1
                return False
        return False
        
                