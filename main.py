class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # base case
        if head is None:
            return
        
        if head.val == val:
            head = self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
        
        return head
