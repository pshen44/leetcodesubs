# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        lnode, rnode = dummy, dummy
        Lprev = prev = None
        while left:
            Lprev = lnode
            lnode = lnode.next
            left -= 1
            rnode = rnode.next
            right -= 1
        while right:
            nxt = rnode.next
            rnode.next = prev
            prev = rnode
            rnode = nxt
            right -= 1
        rlast = rnode.next
        rnode.next = prev
        lnode.next = rlast
        Lprev.next = rnode
        return dummy.next

