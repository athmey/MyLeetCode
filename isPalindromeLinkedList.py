# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        # find the length of this linked list
        cur = head
        length = 0

        while cur is not None:
            length +=1
            cur = cur.next

        # Then break the list into 2 parts depending on the list length
        cur = head
        firstpart = head

        if length % 2 == 0:
            midstep = length//2
        else:
            midstep = length//2 + 1

        secondpart = head
        for i in range(midstep):
            secondpart = secondpart.next

        # reverse the second part
        dummyhead = ListNode(-1)
        dummyhead.next = secondpart

        prev = dummyhead
        cur = secondpart
        next = secondpart.next

        while next is not None:
            cur.next = prev
            prev = cur
            cur = next
            next = next.next

        cur.next = prev
        secondpart = cur

        # compare the 2 parts
        for i in range(length//2):
            if firstpart.val != secondpart.val:
                return False
            firstpart = firstpart.next
            secondpart = secondpart.next

        return True












