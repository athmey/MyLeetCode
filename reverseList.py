# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None:
            return head

        dummyhead = ListNode(-1)

        # 3 pointers

        prev = dummyhead
        cur = head
        next = head.next

        while next is not None:
            # 预防dummynode被嵌入列表
            if cur is head:
                cur.next = None

            else:
                cur.next = prev
            prev = cur
            cur = next
            next = next.next

        # 临界条件，最后三个节点操作完的下一次操作
        cur.next = prev

        return cur