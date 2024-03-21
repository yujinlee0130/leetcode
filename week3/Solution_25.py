# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return
        
        curr = head
        headpointer = head
        prev = None
        counter = 0

        # don't reverse if less than k nodes left
        checkcurr = head
        checkcounter = 0
        while checkcurr != None:
            checkcurr = checkcurr.next
            checkcounter += 1
        if checkcounter < k: return head
        print(checkcounter)

        # reverse if >= k nodes left
        while counter < k and curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            counter += 1
        
        # new tail should point to the new head
        headpointer.next = self.reverseKGroup(curr, k)
        
        return prev
            
            
        
        

