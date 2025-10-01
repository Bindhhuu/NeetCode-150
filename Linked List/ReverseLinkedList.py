class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next     # save next node
            curr.next = prev    # reverse pointer
            prev = curr         # move prev forward
            curr = nxt          # move curr forward
        
        return prev   # prev becomes the new head
#tc: O(n)
#sc: O(1)
