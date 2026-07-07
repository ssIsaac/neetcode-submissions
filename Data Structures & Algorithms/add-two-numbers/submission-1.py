# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:    
        sum = []
        while(l1):
            sum.append(l1.val)
            l1 = l1.next
        

        count = 0
        while(l2):
            if(count >= len(sum)):
                sum.append(l2.val)
            else:
                sum[count] += l2.val
                count += 1
            l2 = l2.next


        head = ListNode()
        curr = head
        count = 0
        while(curr.val >= 10 or count < len(sum)):
            bringOver = 0
            if(count < len(sum)):
                bringOver = sum[count]
            if(curr.val >= 10):
                bringOver += curr.val // 10
                curr.val = curr.val%10 
            nextNode = ListNode(bringOver)
            curr.next = nextNode
            curr = curr.next
            count += 1

        return head.next


        
            
