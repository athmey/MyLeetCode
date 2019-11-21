# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        cur1 = head # 每次走1步
        cur2 = head # 每次走2步

        while cur1 is not None:
            cur1 = cur1.next

            if cur2 is not None and cur2.next is not None and cur2.next.next is not None:
                cur2 = cur2.next.next
            else:
                return False

            if cur1 is cur2:
                return True

        return False