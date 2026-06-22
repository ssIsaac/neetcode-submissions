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

        if(lst):
            if(r >= 0):
                res = lst[r][0]
            elif(lst[l][1] < timestamp):
                res = lst[l][0]

        return res



        
        
