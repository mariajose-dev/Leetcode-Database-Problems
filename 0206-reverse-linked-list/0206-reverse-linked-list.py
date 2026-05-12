# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        cur = head

        while cur:

            nxt = cur.next   # store next node

            cur.next = prev  # reverse pointer

            prev = cur       # move prev
            cur = nxt        # move current

        return prev
