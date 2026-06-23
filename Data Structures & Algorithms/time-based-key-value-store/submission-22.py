class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append([value, timestamp])
        


    def get(self, key: str, timestamp: int) -> str:
        lst = self.time[key]
        l,r = 0, len(lst)-1
        res = ""
        while(l <= r):
            mp = (l+r)//2

            # if(lst[mp][1] <= timestamp):
            #     res = lst[mp][0]
            #     l = mp + 1
            # else:
            #     r = mp - 1
            if(lst[mp][1] == timestamp):
                return lst[mp][0]
            elif(lst[mp][1] > timestamp):
                r = mp - 1
            else:
                l = mp + 1

        """
        because r will always end up in the position that is the largest value smaller than timestamp
        and l will always end up in the position that is the smallest value latger than timestamp 
        ie. [1,3,4,5,7,9] timestamp = 6, l = index4, r = index3

        edge case is if r = -1, l=0, meaning there is no valid value to return since -1 means rightmost element 
        lst=[[one,10],[two,20]], timestamp=5 - there should be no answer since timestamp < 10

        """
        if(lst and r >= 0):
            res = lst[r][0]
        

        return res



        
        
