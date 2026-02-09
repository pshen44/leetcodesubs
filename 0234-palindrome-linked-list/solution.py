# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = deque()
        prev = None
        cur = head
        while cur:
            q.append(cur.val)
            NXT = cur.next
            cur.next = prev
            prev = cur
            cur = NXT
        while prev:
            if prev.val == q[0]:
                q.popleft()
            prev = prev.next
        return True if not q else False

        


