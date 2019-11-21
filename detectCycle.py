# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None

        cur1 = head # 每次走1步
        cur2 = head # 每次走2步
        encounter_point = None
        counter = 0 # 记录两个指针行走的步数

        # 先判断有没有环，并记录下两者相遇的位置，两者相遇的位置必然在环里
        # 利用counter记录下两个指针的移动次数
        while cur1 is not None:
            cur1 = cur1.next

            if cur2 is not None and cur2.next is not None and cur2.next.next is not None:
                cur2 = cur2.next.next

            # 链表无环，cur2才可能等于None
            else:
                return None

            counter += 1

            if cur1 is cur2:
                encounter_point = cur2
                break
        '''
        解题思路：
            https://blog.csdn.net/Eartha1995/article/details/80990636
        '''
        cur1 = head
        cur2 = encounter_point

        if cur1 is cur2:
            return cur1

        while True:
            cur1 = cur1.next
            cur2 = cur2.next

            if cur1 == cur2:
                print('!!!!')
                break

        return cur1