# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow,fast = head, head.next
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            # print(fast.val)
            ## sec half of the list is always slow + 1
        
        # slow.next = None
        reversed = self.reverseList(slow.next)
        slow.next = None

        
        first,second = head, reversed
        while (second):
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1, tmp2



    
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head 
        if(head.next):
            newHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return newHead
        
        