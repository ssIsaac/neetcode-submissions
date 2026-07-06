"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Traverse through the main list
at every node, check if node is in dictionary (oldNode:newNode)
if inside, just assign
if not, create and add into the dictionary

node.random - check if node is in dictionary first 
if pointed node is in dictionary ie. element behind, just assign
if pointed node is not in dictionary ie. element in front, create and store in dictionary

"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # tmp = defaultdict(int)

        # curr, prev = head, head
        # newList = Node(0)
        # newCurr = newList
        # while(curr.next):

        #     if(curr not in tmp):
        #         tmp1 = Node(curr.val)
        #         if curr.random not in tmp:
        #             if not curr.random:
        #                 break
        #             tmp2 = Node(curr.random.val)
        #             tmp[curr.random] = tmp2
        #         else:
        #             tmp1.random = tmp[curr.random]
        #         tmp[curr] = tmp1

        #     newCurr.next = tmp[curr]
        #     newCurr = newCurr.next
        #     curr = curr.next

        # return newList.next


        oldToNew = {None:None}

        curr = head
        while(curr):
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while(curr):
            tmp = oldToNew[curr]
            tmp.next = oldToNew[curr.next]
            tmp.random = oldToNew[curr.random]            
            curr = curr.next

        return oldToNew[head]
        


                
