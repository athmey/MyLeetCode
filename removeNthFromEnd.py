# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head

        if head.next is None and n is 1:
            return None

        dummy_head = ListNode(-1)
        dummy_head.next = head

        current = dummy_head.next
        target = dummy_head.next
        prev = dummy_head

        counter = 1

        while current is not None:

            while counter <= n:
                current = current.next
                counter +=1

            if current is not None:
                current = current.next
                target = target.next
                prev = prev.next

        prev.next = prev.next.next

        return dummy_head.next

