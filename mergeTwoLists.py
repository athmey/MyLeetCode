# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None

        if l1 is None and l2 is not None:
            return l2

        if l1 is not None and l2 is None:
            return l1

        current_l1_pointer = l1
        current_l2_pointer = l2

        dummy_node = ListNode(-1)
        current_newlist_pointer = dummy_node

        while current_l1_pointer is not None and current_l2_pointer is not None:

            if current_l1_pointer.val < current_l2_pointer.val:
                current_newlist_pointer.next = current_l1_pointer
                current_newlist_pointer = current_newlist_pointer.next

                current_l1_pointer = current_l1_pointer.next

            else:
                current_newlist_pointer.next = current_l2_pointer
                current_newlist_pointer = current_newlist_pointer.next

                current_l2_pointer = current_l2_pointer.next

        if current_l1_pointer is None:
            current_newlist_pointer.next = current_l2_pointer

        else:
            current_newlist_pointer.next = current_l1_pointer

        return dummy_node.next