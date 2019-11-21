# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        # 计算链表的总长度
        cur = head
        counter = 0

        while cur is not None:
            cur = cur.next
            counter +=1

        # 寻找中点
        mid = counter //2 + 1
        counter = 1
        cur = head

        while counter < mid:
            cur = cur.next
            counter +=1

        return cur
