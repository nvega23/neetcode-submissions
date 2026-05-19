# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy, curr = None, head

        while curr is not None:
            nxt = curr.next
            curr.next = dummy
            dummy = curr
            curr = nxt
        return dummy