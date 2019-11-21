# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummy_head = ListNode(head.val + 1)
        dummy_head.next = head

        repeated_vals = set()

        cur = head
        next = head.next

        while next is not None:
            if next.val == cur.val:
                repeated_vals.add(next.val)
            next = next.next
            cur = cur.next

        prev = dummy_head
        cur = head
        next = head.next

        while cur is not None:
            if cur.val in repeated_vals:
                cur = cur.next
                prev.next = cur


            else:
                prev = prev.next
                cur = cur.next

        return dummy_head.next

