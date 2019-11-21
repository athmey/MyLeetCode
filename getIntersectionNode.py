# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
'''

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 先找到两个链表各自的长度
        A_list_length = 0
        B_list_length = 0

        cur_A = headA
        cur_B = headB

        while cur_A is not None:
            cur_A = cur_A.next
            A_list_length +=1

        while cur_B is not None:
            cur_B = cur_B.next
            B_list_length +=1

        cur_A = headA
        cur_B = headB

        if A_list_length > B_list_length:
            for i in range(A_list_length - B_list_length):
                cur_A = cur_A.next
        else:
            for i in range(B_list_length - A_list_length):
                cur_B = cur_B.next

        while cur_A is not None and cur_B is not None:
            if cur_B is cur_A:
                return cur_A

            # print('A:', cur_A.val)
            # print('B:', cur_B.val)
            cur_A = cur_A.next
            cur_B = cur_B.next

        return None