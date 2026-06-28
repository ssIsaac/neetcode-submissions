# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(head == None):
            return None
        curr, prev = head, None
        # print(head)

        while(head.next):
            curr = head.next 
            head.next = prev
            # print(curr.val)
            prev = head
            head = curr

        head.next = prev
        

        return head


