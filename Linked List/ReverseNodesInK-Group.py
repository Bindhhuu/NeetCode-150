# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        def getlen(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        length = getlen(head)

        while length >= k:
            curr = prev.next
            nextt = curr.next

            for _ in range(k-1):
                curr.next = nextt.next
                nextt.next = prev.next
                prev.next = nextt
                nextt = curr.next

            prev = curr
            length -= k

        return dummy.next
        
