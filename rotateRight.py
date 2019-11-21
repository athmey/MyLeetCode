# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        dummy_head = ListNode(-1)
        dummy_head.next = head

        prev = dummy_head
        cur = head

        counter = 0

        while cur != None:
            counter +=1
            cur = cur.next
            prev = prev.next

        if k >= counter:
            k = k % counter

        new_cur = head
        for i in range(counter - k - 1):
            new_cur = new_cur.next

        prev.next = dummy_head.next
        dummy_head.next = new_cur.next
        new_cur.next = None


        return dummy_head.next