# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None

        dummy_head = ListNode(-1)
        dummy_head.next = head

        current = head
        prev = dummy_head

        while current is not None:

            if current.val != val:
                current = current.next
                prev = prev.next

            else:
                current = current.next
                prev.next = current

        return dummy_head.next