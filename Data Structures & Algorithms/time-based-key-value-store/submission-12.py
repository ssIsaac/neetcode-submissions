class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append([value, timestamp])
        


    def get(self, key: str, timestamp: int) -> str:
        ## if key (name) does not exist, return ""
        ## if timestamp is not found and no record of timestamp_prev, return ""
        lst = self.time.get(key) ## [[a,1], [b,3], [c,4]]
        if not lst:
            lst = []
        res = ""
        l,r = 0, len(lst)-1
         
        while(l <= r):
            mp = (l+r)//2
            
            if(lst[mp][1] <= timestamp):
                res = lst[mp][0]
                l = mp + 1
            else:
                r = mp - 1

        return res

        
