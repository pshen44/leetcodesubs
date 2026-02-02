# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        prev = slow.next = None
        while l2:
            nxt = l2.next
            l2.next = prev
            prev = l2
            l2 = nxt
        
        l1, l2 = head, prev
        while l2:
            nxt1 = l1.next
            nxt2 = l2.next
            l1.next = l2
            l2.next = nxt1
            l1 = nxt1
            l2 = nxt2
