"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        count,res = 0,0
        
        startCounter, endCounter = 0, 0
        while startCounter < len(start):
                if(start[startCounter] < end[endCounter]):
                    startCounter += 1
                    count += 1
                else:
                    endCounter += 1
                    count -= 1
                res = max(count, res)
                
        return res



        
        