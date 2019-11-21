# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        else:
            cur = head

            dummy_head = ListNode(cur.val + 1)
            dummy_head.next = head

            prev = dummy_head

            prevIsDummy = True

            while cur is not None:
                if cur.val != prev.val:
                    cur = cur.next
                    prev = prev.next

                else:
                    cur = cur.next
                    prev.next = cur

        return dummy_head.next
